# TODO ERIC: This is a mess and the methods that work with templates seem Very Bad at my resolution. Go back to other path.

import cv2 as cv
import numpy as np
import time
import string

THRESHOLD = .96

img_rgb = cv.imread('samples/SHITTY_U_exotic_a1_letters.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

# TODO this
def get_color(a, b, c, d, e):
  return "red"

def print_results(sorted_letters):
  for line in range(sorted_letters[-1]['line_number'] + 1):
    # TODO ERIC ugh how to pipe where is my elixir
    line_letters = list(filter(lambda x: x['line_number'] == line, sorted_letters))

    end_of_last_letter_x = line_letters[0]['x'] + line_letters[0]['width']
    last_color = line_letters[0]['color']
    spaced_letters = ["(" + last_color + ") "]

    for letter in line_letters:
      if letter['color'] != last_color:
        spaced_letters.append("\n(" + letter['color'] + ") ")
        last_color = letter['color']
      x_diff = letter['x'] - end_of_last_letter_x
      # TODO add more spaces if it's really big
      if x_diff > 7:
        spaced_letters.append(" ")
      end_of_last_letter_x = (letter['x'] + letter['width'])
      spaced_letters.append(letter["letter"])

    print("".join(spaced_letters))

print("Let's go!")

# all_letters = list(string.ascii_uppercase)
all_letters = ['U', 'P']
results = []
for key in all_letters:
  # Lowercase
  template = cv.imread("mask_keys/" + key + "_lower_key.png", 0)
  mask = cv.imread( "mask_keys/" + key + "_lower_mask.png", 0 )
  w, h = template.shape[::-1]
  # two methods accept masks:
  # method_accepts_mask = (cv.TM_SQDIFF == match_method or match_method == cv.TM_CCORR_NORMED)
  # All methods: SQDIFF \n 1: SQDIFF NORMED \n 2: TM CCORR \n 3: TM CCORR NORMED \n 4: TM COEFF \n 5: TM COEFF NORMED

  # Eric note: TM_CCOEFF_NORMED seems to take a mask and do some work?
  # res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
  if mask is None:
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
  else:
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED, None, mask)

  # Res is two arrays, one x and one Y

  loc = np.where( res >= THRESHOLD)
  points_found = 0
  for pt in zip(*loc[::-1]):
    points_found +=1
    results.append({'x': pt[0], 'y': pt[1], 'letter': key.lower(), 'width': w, 'height': h, 'color': get_color(img_rgb, pt[0], pt[1], w, h)})
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,0,255), 1)

cv.imwrite('res.png',img_rgb)
# Uppercase
  # template = cv.imread("keys/" + key + "_upper_key.png", 0)
  # w, h = template.shape[::-1]
  # # two methods accept masks:
  # # method_accepts_mask = (cv.TM_SQDIFF == match_method or match_method == cv.TM_CCORR_NORMED)
  # res = cv.matchTemplate(img_gray, template, cv.TM_CCORR_NORMED)
  # loc = np.where( res >= THRESHOLD)
  # for pt in zip(*loc[::-1]):
  #   results.append({'x': pt[0], 'y': pt[1], 'letter': key, 'width': w, 'height': h, 'color': get_color(img_rgb, pt[0], pt[1], w, h)})


    # for hit in pyautogui.locateAll("keys/" + key + "_upper_key.png", im, confidence=0.96, grayscale=True):
    # results.append({'x': hit.left, 'y': hit.top, 'letter': key, 'width': hit.width, 'color': get_color(im, hit.left, hit.top, hit.width, hit.height)})

print("Bucket Time")
y_sorted = sorted(results, key=lambda letter: letter['y'])

current_line_number = 0
if len(y_sorted) == 0:
  print("I got no results.")
  exit()

current_row_y = y_sorted[0]['y']
for letter in y_sorted:
  if letter['y'] - current_row_y <= 7:
    letter['line_number'] = current_line_number
  else:
    current_line_number += 1
    current_row_y = letter['y']
    letter['line_number'] = current_line_number

multisorted = sorted(results, key = lambda x: (x['line_number'], x['x']))

print_results(multisorted)


# for result in multisorted:
#   print(result)

# cv.imwrite('res.png', img_rgb)
