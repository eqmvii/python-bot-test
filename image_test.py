import pyautogui
import time
import PIL
from PIL import Image

# im = pyautogui.screenshot()
im = Image.open("samples/sample_items_screenshot.png")

print(im.mode)
# RGB

grayimg = im.convert('L')
print(grayimg.mode)

print(im.getpixel((0,0)))
# (50, 50, 1)

print(grayimg.getpixel((0,0)))
# 50

grayimg.save("samples/gray.png")
# for x in range(grayimg.width):
#     for y in range(grayimg.height):
#       print(grayimg.getpixel((x, y)))

binary = im.convert('1')

binary.save("samples/binary.png")
