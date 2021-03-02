import pyautogui


# confidence works well for finding super in potion in a test. Required installing opencv-python
# sp = pyautogui.locateCenterOnScreen('L_cap_green.png', confidence=0.9)

# sp = pyautogui.locateAllOnScreen('A_lower_green.png', confidence=0.9)

# for i in sp:
#   print(i)
# print(sp)

chars = pyautogui.locateAllOnScreen('L_lower_green.png', confidence=0.9)

total = 0
for i in chars:
  total += 1
  # print(i)

print("Found " + str(total) + " chars.")
