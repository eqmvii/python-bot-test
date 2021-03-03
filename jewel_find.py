# pyautogui.click()
#
# Demo - detect a set item on the ground, pick it up if there is one
#
import pyautogui
import time

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

centerX = screenWidth / 2
centerY = screenHeight / 2

pyautogui.moveTo(centerX, centerY)

pyautogui.click()

time.sleep(1)

pyautogui.keyDown('alt')

magic_jewel_hits = pyautogui.locateAllOnScreen("words/blue_jewel.png", confidence=0.9)

for magic_jewel in magic_jewel_hits:
  pyautogui.moveTo(magic_jewel)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(1.5)

rare_jewel_hits = pyautogui.locateAllOnScreen("words/yellow_jewel.png", confidence=0.9)

for rare_jewel in rare_jewel_hits:
  pyautogui.moveTo(rare_jewel)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(1.5)

pyautogui.keyUp('alt')
