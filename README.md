# MediaRemote_ABShutter3

This Python script turns a Bluetooth selfie remote (like **AB Shutter 3**) into a media controller on your PC.

When you press the remote's **"Volume Up"** button, it triggers:

- ▶️ **Play/Pause** of your media player  
- 🔉 **Volume Down** on your system  

---

## 📦 Features

- Detects Bluetooth key events from selfie remotes
- Simulates system-level **media control** using `pyautogui` and `keyboard`
- Customizable keys
- Simple console feedback
- Easy to stop (press `Esc`)

---

## 🚀 How It Works

The remote sends **Volume Up** and **Volume Down** key events.  
This script listens for `volume up`, and when detected, triggers:

1. **Play/Pause** media (via `pyautogui`)
2. Short delay
3. **Volume Down** (via `keyboard.send`)

---

## 🛠️ Requirements

Install dependencies:

```bash
pip install pyautogui keyboard
