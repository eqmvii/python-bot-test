import pyautogui
from datetime import datetime
import time
import sys
import numpy as np

## Custom Modules
import reading_glasses
import logger
import rejects
import reject_runes

SLEEP_TIME = 0.25
WALK_TIME = 1.15
TELE_TIME = 0.22

CENTER_X = 960
CENTER_Y = 540

WORD_CONFIDENCE = 0.85

ITEMS_TO_REJECT = rejects.list_items()
RUNES_TO_REJECT = reject_runes.list_items()

# TODO const region tuple?

def go_n_wait(x, y):
  pyautogui.moveTo(x, y)
  pyautogui.click()
  time.sleep(WALK_TIME)


def tele_n_wait(x, y, delay=TELE_TIME):
  pyautogui.moveTo(x, y)
  pyautogui.click(button='right')
  time.sleep(delay)

def should_loot(item_color, item_name):
  if item_color == "red" and item_name not in RUNES_TO_REJECT:
    pyautogui.screenshot("run_screens/hr_drops/" + item_name + "_" + datetime.now().strftime("%m.%d.%Y.at.%H.%M.%S") + '.png', region=(566,218, 790, 590))
    return True
  elif item_color == "red":
    logger.log("I saw, but rected, this rune during rune only mode: " + item_name)
    return False
  else:
    return False

def loot():
  items_looted = 0
  attempts = 0

  while True:
    attempts += 1
    found_something_this_scan = False
    pyautogui.moveTo(580, 240)
    pyautogui.keyDown('alt')
    time.sleep(0.1)

    items = reading_glasses.teach_me_how_to_read(pyautogui.screenshot(region=(566,218, 790, 590)))

    for item in items:
      if should_loot(item.color, item.identity):
        items_looted += 1
        found_something_this_scan = True
        logger.log("Picking up " + item.full_name() + " at (" + str(item.pickup_x() + 566) + ", " + str(item.pickup_y() + 218) + ")")
        # Add in the start points for the screenshot
        pyautogui.moveTo(item.pickup_x() + 566, item.pickup_y() + 218)
        time.sleep(0.3)
        pyautogui.click()
        time.sleep(2)
        break

    if not found_something_this_scan:
      break

    if attempts > 2:
      logger.log("Full Inventory or pickup bug, can't proceed")
      # Pause the game and stop the bot.
      pyautogui.keyUp('alt')
      pyautogui.keyDown('escape')
      sys.exit()

  pyautogui.keyUp('alt')
  return items_looted

# STATS: 128% FCR, 25% R/W, 80% FHR, 950 life 840 mana
def run_bot():
  items_picked = 0

  time.sleep(0.6)
  pyautogui.moveTo(600, 260) # random click, if it was first game open, gets to title screen
  pyautogui.click()

  sp = pyautogui.locateCenterOnScreen('single_player.png', region=(600, 300, 790, 590), grayscale=True)
  pyautogui.moveTo(sp)
  pyautogui.click()
  time.sleep(SLEEP_TIME)

  sf = pyautogui.locateCenterOnScreen('sorcyfindo.png', confidence=0.8, region=(566, 300, 790, 590), grayscale=True)
  pyautogui.moveTo(sf)
  pyautogui.click()
  pyautogui.click()

  pyautogui.press('h') # Choose Hell

  time.sleep(0.8) # Enter game

  # Freeze up

  pyautogui.press('f4') # Frozen Armor
  time.sleep(0.1)
  pyautogui.click(button='right')

  pyautogui.press('f3') # Select TK
  time.sleep(0.2)

  pyautogui.moveTo(1070, 458) # Get a little closer to the wp
  pyautogui.click()
  time.sleep(0.3)

  pyautogui.moveTo(1138, 366) # TK the WP
  pyautogui.click(button='right')
  time.sleep(0.5)

  pyautogui.moveTo(793, 308) # Act III tab
  pyautogui.click()
  time.sleep(0.4)

  pyautogui.moveTo(674, 510) # LK WP
  pyautogui.click()
  time.sleep(0.4)

  pyautogui.press('f2') # Select TP
  time.sleep(0.1)

  pyautogui.moveTo(1236, 695) # Right of portal
  pyautogui.click(button='right')
  time.sleep(0.2)

  pyautogui.moveTo(1289, 680) # Into the hut
  pyautogui.click(button='right')
  time.sleep(0.2)

  pyautogui.moveTo(937, 514) # Click the first chest
  pyautogui.click()
  time.sleep(0.2)

  # First loot attempt: First chest
  items_picked += loot()

  pyautogui.press('f3') # Select TK
  time.sleep(0.1)

  pyautogui.moveTo(1235, 586) # TK the 2nd chest
  pyautogui.click(button='right')

  pyautogui.press('f2') # Re-select Teleport
  time.sleep(0.1)

  # Tele right a little, try looting again
  pyautogui.moveTo(1354, 703)
  pyautogui.click(button='right')
  time.sleep(0.4)

  # Second loot attempt: lower chest
  items_picked += loot()

  for i in range(9):
    # Tele a little left
    pyautogui.moveTo(774, 400)
    pyautogui.click(button='right')
    time.sleep(0.1)

    wp = pyautogui.locateCenterOnScreen('lk_wp.png', confidence=0.8, region=(566,218, 790, 590), grayscale=True)

    if wp:
      pyautogui.moveTo(wp)
      pyautogui.press('f3') # Select TK
      time.sleep(0.1)
      pyautogui.click(button='right')
      time.sleep(0.4)

      pyautogui.moveTo(858, 307) # Act IV tab
      pyautogui.click()
      time.sleep(0.4)

      pyautogui.moveTo(676, 369) # Pandemonium Fortress
      pyautogui.click()
      time.sleep(0.7)

      pyautogui.press('esc') # Leave the game
      time.sleep(0.2)

      pyautogui.moveTo(CENTER_X, (CENTER_Y - 40))
      pyautogui.click()

      return items_picked


  print("I broke.")
  pyautogui.press('esc')
  raise

def main():
  print("Begin LK Runs\n")
  finds = 0
  bot_start = time.time()

  for i in range(1, 401):
    logger.log("LK Two Chest Run", "lk")
    run_start = time.time()
    finds += run_bot()
    avg_run = str(round((time.time() - bot_start) / i, 2))
    print("| Run  " + str(i) + " took " + str(round((time.time() - run_start), 2)) + " sec. Avg: " + avg_run + " sec. Found: " + str(finds) + "|")

  print("Goodbye!")

if __name__ == "__main__":
  main()
