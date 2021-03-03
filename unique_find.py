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

chars = ['A', 'E', 'O', 'U', "R", "S", "D", "N", "G"]

for c in chars:
  print("Finding " + c + "...")
  # hit = pyautogui.locateCenterOnScreen("gold_letters/" + c + '_lower_gold.png', confidence=0.9)
  hits = pyautogui.locateAllOnScreen("gold_letters/" + c + '_lower_gold.png', confidence=0.75)
  # chars = pyautogui.locateAllOnScreen('L_lower_gold.png', confidence=0.9)

  for hit in hits:
    if str(hit) != "None":
      print(hit)
      # Unique color is 148, 128, 100
      im = pyautogui.screenshot()
      orig_x = int(hit[0])
      orig_y = int(hit[1])

      spread = 3
      gold = 0
      total = 0
      for x in range(orig_x - spread, orig_x + spread):
        for y in range(orig_y - spread, orig_y + spread):
          total += 1
          pix = im.getpixel((x - 1, y - 1))
          # print(pix)
          if ((148, 128, 100) == pix):
            gold +=1
      # print("Gold Pixels: " + str(gold) + "out of " + str(total) + " pixels")
      if gold > 0:
        pyautogui.moveTo(hit)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(2)


time.sleep(0.5)

pyautogui.keyUp('alt')
print("done")

# total = 0
# for i in chars:
#   total += 1
#   # print(i)

# print("Found " + str(total) + " chars.")
