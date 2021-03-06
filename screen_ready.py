import pyautogui
import time
import string
import PIL
import reading_glasses
from PIL import Image

while True:
  time.sleep(.5)
  items = reading_glasses.teach_me_how_to_read(pyautogui.screenshot(region=(566,218, 790, 590)))

