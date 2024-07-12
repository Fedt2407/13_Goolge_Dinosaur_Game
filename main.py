import time
import pyautogui
from PIL import ImageGrab
import webbrowser

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.keyUp('space')

def detect_collision(data):
    # Check collision for birds (upper part)
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                return True
    # Check collision for cactus (lower part)
    for i in range(415, 475):
        for j in range(410, 563):
            if data[i, j] < 100:
                return True
    return False

def main():
    # Open the game in Chrome
    webbrowser.open("chrome://dino")

    # Give some time for the browser to open
    time.sleep(5)

    # Set the game window as the active window
    pyautogui.click(300, 300)  # Click on the game window to make it active

    while True:
        # Capture the screen
        image = ImageGrab.grab().convert('L')
        data = image.load()

        # Check if the dinosaur must jump
        if detect_collision(data):
            jump()

if __name__ == '__main__':
    main()
