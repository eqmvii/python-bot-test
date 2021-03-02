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

time.sleep(2)

pyautogui.keyDown('alt')

chars = ['A', 'E', 'I', 'O', 'U']

for c in chars:
  print("Finding " + c + "...")
  hit = pyautogui.locateCenterOnScreen("green_letters/" + c + '_lower_green.png', confidence=0.9)
  # chars = pyautogui.locateAllOnScreen('L_lower_green.png', confidence=0.9)
  print(hit)
  if str(hit) != "None":
    print("ERIC: GOT A HIT FOR " + c)
    pyautogui.moveTo(hit)
    time.sleep(0.2)
    pyautogui.click()
    break

time.sleep(2)

pyautogui.keyUp('alt')

# total = 0
# for i in chars:
#   total += 1
#   # print(i)

# print("Found " + str(total) + " chars.")
