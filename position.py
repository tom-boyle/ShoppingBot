import pyautogui
import time

print("Hover over the location and press Enter")
input()  # Wait for the user to press Enter
position = pyautogui.position()  # Get the mouse cursor's current position
print(f"The coordinates are {position}")
