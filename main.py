import pyautogui
import time

# Open the start menu (Windows key)
pyautogui.hotkey('win')

# Wait for the start menu to open
time.sleep(2)

# Type the name of the web browser you want to open
pyautogui.write('DuckDuck')  # replace 'Chrome' with the name of your web browser
pyautogui.press('enter')

# Wait for the web browser to open
time.sleep(5)

# Type the URL of the webpage you want to open
pyautogui.write('https://marketplace.ticketek.com.au/')  # replace with your webpage URL
pyautogui.press('enter')

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