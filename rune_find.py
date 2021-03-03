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

rune_hits = pyautogui.locateAllOnScreen("words/rune.png", confidence=0.9)

for rune in rune_hits:
  pyautogui.moveTo(rune)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(1.5)

pyautogui.keyUp('alt')
