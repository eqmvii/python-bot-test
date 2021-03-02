# python ocr_test.py
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import cv2

print("hello")

# Added to path
# C:\Program Files\Tesseract-OCR

# tesseract --version works

custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(cv2.imread('single_player.jpg'), config=custom_config))
