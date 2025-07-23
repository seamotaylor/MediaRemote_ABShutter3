import keyboard  # To detect key presses
import pyautogui  # To control system actions (e.g., media keys)
import time

# Constants for key names
SELFIE_BUTTON_KEY = 'volume up'  # Can be customized
EXIT_KEY = 'esc'
VOLUME_DOWN_KEY = 'volume down'
MEDIA_PLAY_PAUSE_KEY = 'playpause'

# Initialization message
print("Initializing... Please wait.")
time.sleep(0.5)

# Function to simulate Play/Pause and Volume Down key presses
def on_selfie_button_press():
    try:
        print("Selfie button pressed!")

        # Simulate Play/Pause media key
        print("Simulating Play/Pause")
        pyautogui.press(MEDIA_PLAY_PAUSE_KEY)

        time.sleep(0.1)  # Short pause before the next action

        # Simulate Volume Down
        print("Simulating Volume Down")
        keyboard.send(VOLUME_DOWN_KEY)  # Single 'tap' function to handle press/release
    except Exception as e:
        print(f"Error during key simulation: {e}")

# Main loop to detect key press events
def main():
    print(f"Press the '{SELFIE_BUTTON_KEY}' to simulate actions... Press '{EXIT_KEY}' to exit.")

    try:
        while True:
            event = keyboard.read_event()

            if event.event_type == keyboard.KEY_DOWN:
                if event.name == SELFIE_BUTTON_KEY:
                    on_selfie_button_press()
                elif event.name == EXIT_KEY:
                    print("Exiting...")
                    break
    except KeyboardInterrupt:
        print("Script interrupted manually. Exiting...")

if __name__ == "__main__":
    main()