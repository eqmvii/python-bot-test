import pyautogui
import time
import sys
import numpy as np

## Custom Modules
import reading_glasses
import logger
import rejects

SLEEP_TIME = 0.25
WALK_TIME = 1.2
TELE_TIME = 0.25

CENTER_X = 960
CENTER_Y = 540

WORD_CONFIDENCE = 0.85

ITEMS_TO_REJECT = rejects.list_items()

# TODO const region tuple?

def go_n_wait(x, y):
  pyautogui.moveTo(x, y)
  pyautogui.click()
  time.sleep(WALK_TIME)


def tele_n_wait(x, y, delay=TELE_TIME):
  pyautogui.moveTo(x, y)
  pyautogui.click(button='right')
  time.sleep(delay)


# TODO ERIC: import module
def write_items(new_items):
  # TODO ERIC: lol why am I opening to read, closing, then opening again to append?
  f_read = open("items.txt", "r")
  existing_items = f_read.readlines()
  f_read.close()

  f = open("items.txt", "a")

  unique_list = set(new_items)
  for new_item in unique_list:
    if new_item + "\n" not in existing_items:
      f.write(new_item + "\n")

  f.close()


def should_loot(item_color, item_name):
  if item_color == 'green' or item_color == 'gold' or item_color == 'red':
    # We're generally interested in set/unique/rune, but reject if we've ID'd something we don't want
    if item_name + "\n" in ITEMS_TO_REJECT:
      logger.log("Choosing _not_ to loot (" + item_color + ") " + item_name)
      return False
    else:
      return True
  if item_name in ["Small Charm", "Grand Charm", "Jewel"]:
    return True
  return False


def loot():
  items_looted = 0
  attempts = 0

  while True:
    attempts += 1
    found_something_this_scan = False
    pyautogui.moveTo(20, 20)
    pyautogui.keyDown('alt')
    time.sleep(0.5)

    items = reading_glasses.teach_me_how_to_read(pyautogui.screenshot(region=(566,218, 790, 590)))
    write_items(map(lambda item: item.name(), items))

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
      print("Nothing to pick up...")
      break

    if attempts > 2:
      logger.log("Full Inventory or pickup bug, can't proceed")
      # Pause the game and stop the bot.
      pyautogui.keyUp('alt')
      pyautogui.keyDown('escape')
      sys.exit()

  pyautogui.keyUp('alt')
  return items_looted

def run_bot():
  items_picked = 0

  time.sleep(0.6)

  sp = pyautogui.locateCenterOnScreen('single_player.png', region=(566,218, 790, 590))
  pyautogui.moveTo(sp)
  pyautogui.click()
  time.sleep(SLEEP_TIME)

  sf = pyautogui.locateCenterOnScreen('sorcyfindo.png', confidence=0.8, region=(566,218, 790, 590))
  pyautogui.moveTo(sf)
  pyautogui.click()
  pyautogui.click()

  hell_button = pyautogui.locateCenterOnScreen('hell.png', region=(566,218, 790, 590))
  pyautogui.moveTo(hell_button)
  pyautogui.click()
  time.sleep(1)

  # Walk to the portal

  go_n_wait(792, 727)
  go_n_wait(761, 661)
  go_n_wait(784, 731)
  go_n_wait(798, 695)
  go_n_wait(932, 735)
  go_n_wait(774, 623)
  go_n_wait(839, 406)
  go_n_wait(780, 470)

  # Inside the portal

  # tstorm
  pyautogui.press('f5')
  time.sleep(0.1)
  pyautogui.click(button='right')
  time.sleep(0.1)
  pyautogui.press('f2')
  time.sleep(0.1)

  tele_n_wait(1225, 309)
  tele_n_wait(1225, 309)
  tele_n_wait(1225, 309)
  tele_n_wait(1180, 430, delay=0)

  # blast 'em

  pyautogui.moveTo(1132, 420)
  pyautogui.keyDown('shift')

  for i in range(11):
    pyautogui.click()
    pyautogui.moveRel(-4, 0)
    time.sleep(0.4)

  pyautogui.keyUp('shift')

  # gimme da loot
  time.sleep(1)

  items_picked += loot()

  # quit the game

  pyautogui.press('esc')
  time.sleep(SLEEP_TIME)
  pyautogui.moveTo(CENTER_X, (CENTER_Y - 40))
  pyautogui.click()
  time.sleep(SLEEP_TIME)

  return items_picked

def main():
  print("Begin Runs 💰")
  finds = 0

  for i in range(1, 61):
    run_start = time.time()
    finds += run_bot()
    print("\n| Run  " + str(i) + ". Found " + str(finds) + " in " + str(round((time.time() - run_start), 2)) + "|\n")

  print("Goodbye 🌊")

if __name__ == "__main__":
  main()
