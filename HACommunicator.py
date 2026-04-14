import pyautogui
import requests
from find_pixel import get_pixel


class HACommunicator:
    def __init__(self, url, token, entity_lst, button_status, lamp_status, brightness=255, transition=0.5):
        self.URL = url
        self.HA_TOKEN = token

        self.ENTITY_LST = entity_lst

        self.BUTTON_STATUS = button_status
        self.LAMP_STATUS = lamp_status
        self.brightness = brightness
        self.transition = transition

        self.headers = {
            "Authorization": f"Bearer {self.HA_TOKEN}",
            "Content-Type": "application/json",
        }

        self.turn_on_url = f"{self.URL}/api/services/light/turn_on"
        self.turn_off_url = f"{self.URL}/api/services/light/turn_off"

    def turn_off(self):
        if self.URL and self.HA_TOKEN and self.ENTITY_LST:
            payload = {
                "entity_id": self.ENTITY_LST,
            }

            response = requests.post(self.turn_off_url, headers=self.headers, json=payload)

            # print("Statuscode:", response.status_code)
            # print("Response:", response.text)
            if response.text == "[]":
                self.LAMP_STATUS.lamp_status = False

    def screen_mode(self, position_lst):
        if self.BUTTON_STATUS:
            self.LAMP_STATUS.lamp_status = True

            all_positions = []
            sample_counts = []

            for pos in position_lst:
                samples = pos.position
                all_positions.extend(samples)
                sample_counts.append(len(samples))

            if not all_positions:
                return

            pixel_colors = get_pixel(all_positions)

            idx = 0
            for i, entity in enumerate(self.ENTITY_LST):
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

                payload = {
                    "entity_id": entity,
                    "rgb_color": [avg_r, avg_g, avg_b],
                    "brightness": self.brightness,
                    "transition": self.transition
                }

                response = requests.post(self.turn_on_url, headers=self.headers, json=payload)

        else:
            if self.LAMP_STATUS.lamp_status:
                self.turn_off()

    def crazy_mode(self):
        if self.BUTTON_STATUS:
            self.LAMP_STATUS.lamp_status = True

            x, y = pyautogui.position()
            pixel_colors = get_pixel([(x, y)])

            for entity in self.ENTITY_LST:
                r, g, b = pixel_colors[0]

                payload = {
                    "entity_id": entity,
                    "rgb_color": [r, g, b],
                    "brightness": self.brightness,
                    "transition": self.transition
                }

                response = requests.post(self.turn_on_url, headers=self.headers, json=payload)
        else:
            if self.LAMP_STATUS.lamp_status:
                self.turn_off()

    def average_mode(self):
        if self.BUTTON_STATUS:
            self.LAMP_STATUS.lamp_status = True
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

            avg_color = [avg_r, avg_g, avg_b]
            for entity in self.ENTITY_LST:
                payload = {
                    "entity_id": entity,
                    "rgb_color": avg_color,
                    "brightness": self.brightness,
                    "transition": self.transition
                }

                response = requests.post(self.turn_on_url, headers=self.headers, json=payload)

        else:
            if self.LAMP_STATUS.lamp_status:
                self.turn_off()
