import pyautogui
import time

SLEEP_TIME = 0.3
WALK_TIME = 1.6
TELE_TIME = 0.35

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

centerX = screenWidth / 2
centerY = screenHeight / 2

def go_n_wait(x, y):
  pyautogui.moveTo(x, y)
  pyautogui.click()
  time.sleep(WALK_TIME)

def tele_n_wait(x, y, delay=TELE_TIME):
  print("delay=" + str(delay))
  pyautogui.moveTo(x, y)
  pyautogui.click(button='right')
  time.sleep(delay)

time.sleep(0.3)

tele_n_wait(1225, 309)
tele_n_wait(1225, 309)
tele_n_wait(1225, 309)
tele_n_wait(1180, 430, delay=0)

# blast 'em

pyautogui.moveTo(1132, 476)
pyautogui.keyDown('shift')

for i in range(6):
  pyautogui.click()
  time.sleep(0.6)

pyautogui.keyUp('shift')

pyautogui.press('esc')

time.sleep(SLEEP_TIME)

pyautogui.moveTo(centerX, (centerY - 40))

pyautogui.click()

time.sleep(SLEEP_TIME)

print("bye")



# # for i in range(1):

# screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

# centerX = screenWidth / 2
# centerY = screenHeight / 2

# currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

# # pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

# # pyautogui.screenshot('foo.png')

# sp = pyautogui.locateCenterOnScreen('single_player.png')

# print(sp)

# pyautogui.moveTo(sp)

# pyautogui.click()

# time.sleep(SLEEP_TIME)

# sf = pyautogui.locateCenterOnScreen('sorcyfindo.png')

# print(sf)

# pyautogui.moveTo(sf)

# pyautogui.click()

# pyautogui.click()

# hell_button = pyautogui.locateCenterOnScreen('hell.png')

# pyautogui.moveTo(hell_button)

# pyautogui.click()

# time.sleep(SLEEP_TIME)

# time.sleep(WALK_TIME)

# # Walk to the portal

# go_n_wait(792, 727)

# go_n_wait(761, 661)

# go_n_wait(784, 731)

# go_n_wait(798, 695)

# go_n_wait(932, 735)

# go_n_wait(774, 623)

# go_n_wait(839, 406)

# go_n_wait(780, 470)

# # Old code

#   # print("done sleeping now moving")

#   # pyautogui.moveRel(-200, 20)

#   # pyautogui.click()

#   # time.sleep(0.8)

#   # pyautogui.click()

#   # time.sleep(0.8)

#   # pyautogui.click()

#   # time.sleep(0.8)

#   # pyautogui.click()

#   # pyautogui.press('esc')

#   # time.sleep(SLEEP_TIME)

#   # pyautogui.moveTo(centerX, (centerY - 40))

#   # pyautogui.click()

#   # time.sleep(SLEEP_TIME)


# # pyautogui.click()          # Click the mouse.
# # pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
# # pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

# # pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.
# # pyautogui.doubleClick()    # Double click the mouse.
# # pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

# # pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# # pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

# # pyautogui.keyDown('shift') # Press the Shift key down and hold it.
# # pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key 4 times.
# # pyautogui.keyUp('shift')   # Let go of the Shift key.

# # pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

# # pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.

# print("END OF SCRIPT")
