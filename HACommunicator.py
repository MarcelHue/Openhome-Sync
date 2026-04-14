import time
import pyautogui
import requests
from find_pixel import get_pixel

COLOR_TOLERANCE = 5
BRIGHTNESS_POLL_INTERVAL = 3.0


class HACommunicator:
    def __init__(self, url, token):
        self.URL = url
        self.HA_TOKEN = token

        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.HA_TOKEN}",
            "Content-Type": "application/json",
        })

        self.turn_on_url = f"{self.URL}/api/services/light/turn_on"
        self.turn_off_url = f"{self.URL}/api/services/light/turn_off"

        self._last_colors = {}
        self._last_brightness = 255
        self._last_brightness_time = 0.0

    def update_credentials(self, url, token):
        if url != self.URL or token != self.HA_TOKEN:
            self.URL = url
            self.HA_TOKEN = token
            self.session.headers["Authorization"] = f"Bearer {self.HA_TOKEN}"
            self.turn_on_url = f"{self.URL}/api/services/light/turn_on"
            self.turn_off_url = f"{self.URL}/api/services/light/turn_off"
            self._last_colors.clear()

    def _color_changed(self, entity, r, g, b, brightness):
        prev = self._last_colors.get(entity)
        if prev is None:
            return True
        pr, pg, pb, pbr = prev
        return (abs(r - pr) > COLOR_TOLERANCE or
                abs(g - pg) > COLOR_TOLERANCE or
                abs(b - pb) > COLOR_TOLERANCE or
                pbr != brightness)

    def _store_color(self, entity, r, g, b, brightness):
        self._last_colors[entity] = (r, g, b, brightness)

    def fetch_brightness(self, brightness_entity, boost):
        now = time.monotonic()
        if now - self._last_brightness_time >= BRIGHTNESS_POLL_INTERVAL:
            if brightness_entity and self.URL and self.HA_TOKEN:
                try:
                    url = f"{self.URL}/api/states/{brightness_entity}"
                    resp = self.session.get(url, timeout=2)
                    if resp.status_code == 200:
                        data = resp.json()
                        self._last_brightness = int(
                            data.get("attributes", {}).get("brightness", 255)
                        )
                except Exception:
                    pass
            self._last_brightness_time = now

        brightness = self._last_brightness
        if boost >= 100:
            brightness = 255
        elif boost > 0:
            brightness = min(255, int(brightness * 100 / (100 - boost)))

        return brightness

    def turn_off(self, entity_lst):
        if self.URL and self.HA_TOKEN and entity_lst:
            payload = {"entity_id": entity_lst}
            try:
                self.session.post(self.turn_off_url, json=payload, timeout=2)
            except Exception:
                pass
            self._last_colors.clear()

    def send_colors(self, entity_color_map, brightness, transition):
        for entity, (r, g, b) in entity_color_map.items():
            if not self._color_changed(entity, r, g, b, brightness):
                continue
            payload = {
                "entity_id": entity,
                "rgb_color": [r, g, b],
                "brightness": brightness,
                "transition": transition,
            }
            try:
                self.session.post(self.turn_on_url, json=payload, timeout=2)
            except Exception:
                pass
            self._store_color(entity, r, g, b, brightness)

    def screen_mode(self, entity_lst, position_data, brightness, transition):
        all_positions = []
        sample_counts = []

        for samples in position_data:
            all_positions.extend(samples)
            sample_counts.append(len(samples))

        if not all_positions:
            return

        pixel_colors = get_pixel(all_positions)

        entity_color_map = {}
        idx = 0
        for i, entity in enumerate(entity_lst):
            if i >= len(sample_counts):
                break
            count = sample_counts[i]
            color_samples = pixel_colors[idx:idx + count]
            idx += count

            if not color_samples:
                continue

            avg_r = sum(c[0] for c in color_samples) // len(color_samples)
            avg_g = sum(c[1] for c in color_samples) // len(color_samples)
            avg_b = sum(c[2] for c in color_samples) // len(color_samples)
            entity_color_map[entity] = (avg_r, avg_g, avg_b)

        self.send_colors(entity_color_map, brightness, transition)

    def crazy_mode(self, entity_lst, brightness, transition):
        x, y = pyautogui.position()
        pixel_colors = get_pixel([(x, y)])
        r, g, b = pixel_colors[0]

        entity_color_map = {entity: (r, g, b) for entity in entity_lst}
        self.send_colors(entity_color_map, brightness, transition)

    def average_mode(self, entity_lst, brightness, transition):
        width, height = pyautogui.size()

        points = [
            (width // 4, height // 4),
            (3 * width // 4, height // 4),
            (width // 4, 3 * height // 4),
            (3 * width // 4, 3 * height // 4),
        ]

        colors = get_pixel(points)

        n = len(colors)
        avg_r = sum(c[0] for c in colors) // n
        avg_g = sum(c[1] for c in colors) // n
        avg_b = sum(c[2] for c in colors) // n

        entity_color_map = {entity: (avg_r, avg_g, avg_b) for entity in entity_lst}
        self.send_colors(entity_color_map, brightness, transition)
