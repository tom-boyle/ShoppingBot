import os
import time
import pyautogui
import webbrowser

# Path to Chrome (change to your path)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'

# URL to open
url = 'https://marketplace.ticketek.com.au/'

# Open Chrome
os.startfile(chrome_path)

# Wait for Chrome to open
time.sleep(5)

# Open URL
webbrowser.open(url)

# Wait for the webpage to load
time.sleep(10)

pyautogui.click(x=1259, y=1000)

time.sleep(10)

while True:
    # Refresh the page
    pyautogui.hotkey('ctrl', 'r')  # use 'command', 'r' on Mac

    # Wait for the page to load
    time.sleep(10)

    # Click specific areas on the screen
    pyautogui.click(x=1016, y=741)   # replace with the coordinates of the first click
    pyautogui.click(x=1414, y=552)  # replace with the coordinates of the second click

    # Wait 2 minutes before refreshing again
    time.sleep(2 * 60)