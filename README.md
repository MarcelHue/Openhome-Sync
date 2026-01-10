# Openhome Sync  
![GitHub all releases](https://img.shields.io/github/downloads/Butter-mit-Brot/Openhome-Sync/total.svg)
![GitHub release](https://img.shields.io/github/v/release/Butter-mit-Brot/Openhome-Sync)
![License](https://img.shields.io/github/license/Butter-mit-Brot/Openhome-Sync)

<img width="908" height="485" alt="image" src="https://github.com/user-attachments/assets/7e8869ec-db22-44e2-9116-a10c8ec1ca4c" />


---

## 📌 What is Openhome Sync?

**Openhome Sync** is an application that synchronizes **Home Assistant light entities** with the **colors of your PC screen**.

My goal was to create a tool similar to **Philips Hue Sync**, but fully integrated into **Home Assistant** - enabling custom Ambilight setups without the Hue ecosystem.

---

## 📥 Installation

### 🪟 Windows (Installer)
Download and install Openhome Sync using the provided Windows installer.

---

### 🛠 DIY / Python Setup
You can also install and run Openhome Sync using Python.

Download the repository and install all required dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use Openhome Sync

### 1️⃣ Enter your Home Assistant IP or domain

<img width="442" height="56" alt="image" src="https://github.com/user-attachments/assets/c3aedb79-c33b-4fa5-9d18-4a38224f7b3c" />

---

### 2️⃣ Enter your **Long-Lived Access Token**

👉 Need help?  
See: <a href="https://github.com/Butter-mit-Brot/Openhome-Sync/tree/main?tab=readme-ov-file#-how-to-get-your-token">**[How to get your token]**</a>

<img width="442" height="50" alt="image" src="https://github.com/user-attachments/assets/d2f78fa3-a419-459b-8090-ff646a1a4a50" />

---

### 3️⃣ Add the entity ID of your light

<img width="433" height="52" alt="image" src="https://github.com/user-attachments/assets/0ef77987-3b06-421e-b09e-7725620edcb3" />

You can:

Add more devices using **+**  
Remove devices using **-**

---

### 4️⃣ Place your lamps on your screen layout

Align the light icons according to their real-world position behind your monitor.

<img width="1112" height="671" alt="image" src="https://github.com/user-attachments/assets/f26f1a81-a027-4c1c-96c8-407f6c208019" />

---

### 5️⃣ Activate Autostart (optional)

<img width="545" height="95" alt="image" src="https://github.com/user-attachments/assets/7be50525-d3ac-4915-b743-fdfa33ef5053" />

You have **3 Autostart options**:

| Mode | Description |
|------|-------------|
| 🔁 **Autostart Application** | Starts Openhome Sync on System startup. |
| ➖ **Autostart minimized** | Always Starts the Application Minimized. |
| 💡 **Autostart Lamps** | Automaticly presses Start on Application Startup. |

**DON'T FORGET TO PRESS SAVE AFTER SELECTING YOUR AUTOSTART OPTIONS**

---

## 🎛 Available Modes

You can choose between **3 different modes**:

| Mode | Description |
|------|-------------|
| 💻 **Screen Mode** | Uses the lamp’s defined position and takes the pixel color from that exact screen spot. |
| 🟰 **Average Mode** | Calculates the average color of 4 predefined screen areas (lamp position doesn’t matter). |
| 😵‍💫 **Crazy Mode** | Uses the color of the pixel currently under your mouse cursor. |

After selecting a mode, press **Start**.  
If setup correctly, your lights will react instantly to your screen’s colors.

---

## 💾 Save & Load Configurations

You can save your entire configuration and load it manually again after restarting the program.

*Your config will be reloaded automaticly after every startup tho.*

<img width="435" height="74" alt="image" src="https://github.com/user-attachments/assets/61dd7c4b-2ca8-48df-b8a0-2a43c6ed312d" />

---

## 🔑 How to get your Token?

Follow these steps in Home Assistant:

### 1️⃣ Open your **User Profile**

<img width="1612" height="914" alt="image" src="https://github.com/user-attachments/assets/8f3a47e8-8e03-4a0f-ac70-073c8c1684c6" />

---

### 2️⃣ Go to the **Security** tab

<img width="1031" height="599" alt="image" src="https://github.com/user-attachments/assets/7ca390ec-7fb8-4ddc-96df-d3d197dd8c3d" />

---

### 3️⃣ Create a **Long-Lived Access Token**

<img width="710" height="369" alt="image" src="https://github.com/user-attachments/assets/2d14abdf-a8a6-46f1-b8ea-87b575cada69" />

---

## ⭐ Feedback & Contributions

If you enjoy the project, feel free to ⭐ star the repository or open issues and pull requests!

---

## 📜 License

This project is licensed under the **GPL 3.0 License**.
