import pyautogui
import reading_glasses
import time

CENTER_X = 960
CENTER_Y = 540

time.sleep(2)

pyautogui.moveTo(CENTER_X, CENTER_Y)

pyautogui.keyDown('alt')
time.sleep(0.5)

items = reading_glasses.teach_me_how_to_read(pyautogui.screenshot(region=(566,218, 790, 590)))

# Naive version - pick up the green and gold and red, only try for one item tops
for item in items:
  if item.color == 'green' or item.color == 'gold' or item.color == 'red':
    print("Picking up " + item.name() + " at (" + str(item.pickup_x() + 566) + ", " + str(item.pickup_y() + 218) + ")")
    # Add in the start points for the screenshot
    pyautogui.moveTo(item.pickup_x() + 566, item.pickup_y() + 218)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(2)
    break

pyautogui.keyUp('alt')
