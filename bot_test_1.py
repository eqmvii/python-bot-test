import pyautogui
import time

SLEEP_TIME = 0.25
WALK_TIME = 1.2
TELE_TIME = 0.25

CENTER_X = 960
CENTER_Y = 540

WORD_CONFIDENCE = 0.8

def go_n_wait(x, y):
  pyautogui.moveTo(x, y)
  pyautogui.click()
  time.sleep(WALK_TIME)

def tele_n_wait(x, y, delay=TELE_TIME):
  pyautogui.moveTo(x, y)
  pyautogui.click(button='right')
  time.sleep(delay)

def loot():
  items_looted = 0
  pyautogui.moveTo(CENTER_X, CENTER_Y)
  pyautogui.keyUp('shift')
  pyautogui.keyDown('alt')

  # Jewels
  # TODO this is grabbing boneweaves which is funny
  magic_jewel_hits = pyautogui.locateAllOnScreen("words/blue_jewel.png", confidence=WORD_CONFIDENCE, region=(566,218, 790, 590))

  for magic_jewel in magic_jewel_hits:
    print("Jewel!")
    items_looted += 1
    pyautogui.moveTo(magic_jewel)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1.5)

  rare_jewel_hits = pyautogui.locateAllOnScreen("words/yellow_jewel.png", confidence=WORD_CONFIDENCE, region=(566,218, 790, 590))

  for rare_jewel in rare_jewel_hits:
    print("Rare jewel!")
    items_looted += 1
    pyautogui.moveTo(rare_jewel)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1.5)

  # Charms
  charm_hits = pyautogui.locateAllOnScreen("words/charm.png", confidence=WORD_CONFIDENCE, region=(566,218, 790, 590))

  for charm in charm_hits:
    print("Charm!")
    items_looted += 1
    pyautogui.moveTo(charm)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1.5)

  # Set Items
  vowels = ['A', 'E', 'I', 'O', 'U']

  for c in vowels:
    hit = pyautogui.locateCenterOnScreen("green_letters/" + c + '_lower_green.png', confidence=0.9, region=(566,218, 790, 590))
    if str(hit) != "None":
      print("Set Item!")
      items_looted += 1
      pyautogui.moveTo(hit)
      time.sleep(0.2)
      pyautogui.click()
      time.sleep(2)

  # Unique Items

  # gold I and D suck, try more distinct letters
  unique_letters = ['A', 'E', 'O', 'U', "R", "S", "D", "N", "G"]

  for c in unique_letters:
    hits = pyautogui.locateAllOnScreen("gold_letters/" + c + '_lower_gold.png', confidence=0.9, region=(566,218, 790, 590))
    for hit in hits:
      # Unique color is 148, 128, 100
      im = pyautogui.screenshot()
      orig_x = int(hit[0])
      orig_y = int(hit[1])

      if c in ["R", "D"]:
        spread = 3
      else:
        spread = 2

      # TODO: Cross instead of square?

      gold = 0
      total = 0
      for x in range(orig_x - spread, orig_x + spread):
        for y in range(orig_y - spread, orig_y + spread):
          total += 1
          pix = im.getpixel((x - 1, y - 1))
          if ((148, 128, 100) == pix):
            gold +=1
      # print("Gold Pixels: " + str(gold) + "out of " + str(total) + " pixels")
      if gold > 0:
        print("Unique!")
        items_looted += 1
        pyautogui.moveTo(hit)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(1.5)

  # Runes

  # TODO: increase confidence or check color? This is grabing rune bows, rune swords, etc.
  rune_hits = pyautogui.locateAllOnScreen("words/rune.png", confidence=WORD_CONFIDENCE, region=(566,218, 790, 590))

  for rune in rune_hits:
    print("Rune!")
    items_looted += 1
    pyautogui.moveTo(rune)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(1.5)

  pyautogui.keyUp('alt')
  return items_looted

def run_bot():
  items_picked = 0

  time.sleep(0.3)

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

  tele_n_wait(1225, 309)
  tele_n_wait(1225, 309)
  tele_n_wait(1225, 309)
  tele_n_wait(1180, 430, delay=0)

  # blast 'em

  pyautogui.moveTo(1132, 420)
  pyautogui.keyDown('shift')

  for i in range(9):
    pyautogui.click()
    pyautogui.moveRel(-5, 0)
    time.sleep(0.5)

  # gimme da loot

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

  for i in range(1, 101):
    finds += run_bot()
    print("| Run  " + str(i) + ". Found " + str(finds))

  print("Goodbye 🌊")

if __name__ == "__main__":
  main()
