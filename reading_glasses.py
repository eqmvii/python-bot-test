# Libraries

import pyautogui
import time
import string
import PIL
from PIL import Image

# Project modules
from GroundItem import GroundItem

def print_results(item_list):
  for item in item_list:
    print(item.full_name())

def build_results(line_sorted_letters):
  if not line_sorted_letters:
    print("No letters to build!")
    return []

  items = []

  for letter in line_sorted_letters:
    if not items:
      items.append(GroundItem(letter))
    else:
      # Different color or different line means new item
      if items[-1].color != letter["color"] or items[-1].line_number != letter["line_number"]:
        items.append(GroundItem(letter))
      else:
        ll = items[-1].last_letter()
        if (letter["x"] - (items[-1].last_letter()["x"] + ll["width"])) > 7:
          # TODO: clone the letter?
          items[-1].add_letter({'capital': ll["capital"], 'x': ll["x"] + ll["width"], 'y': ll["y"], 'line_number': ll["line_number"], 'letter': " ", 'width': 1, 'color': ll["color"]})
        items[-1].add_letter(letter)

  for item in items:
    # Minor performance improvement: only ID things we might pick up
    if item.color in ["red", "green", "blue", "yellow", "gold"]:
      item.identify()

  return items

def get_color(im, x, y, width, height):
  gold_pixels = 0
  green_pixels = 0
  red_pixels = 0
  yellow_pixels = 0
  blue_pixels = 0
  for i in range(width):
    for j in range(height):
      pix = im.getpixel((int(x) + i, int(y) + j))
      if pix == (148, 128, 100):
        gold_pixels += 1
        if gold_pixels >= 2:
          return "gold"
      elif pix == (12, 196, 28):
        green_pixels += 1
        if green_pixels >= 2:
          return "green"
      elif pix == (208, 132, 32):
        red_pixels += 1
        if red_pixels >= 2:
          return "red"
      elif pix == (216, 184, 100):
        yellow_pixels +=1
        if yellow_pixels >= 2:
          return "yellow"
      elif pix == (80, 80, 172):
        blue_pixels +=1
        if blue_pixels >= 2:
          return "blue"
  return "other"

def bucket(raw_results):
  if not raw_results:
    return []
  y_sorted = sorted(raw_results, key=lambda letter: letter['y'])

  current_line_number = 0
  current_row_y = y_sorted[0]['y']
  for letter in y_sorted:
    if letter['y'] - current_row_y <= 12: # 11 dropped a from a super healing potion
      letter['line_number'] = current_line_number
    else:
      current_line_number += 1
      current_row_y = letter['y']
      letter['line_number'] = current_line_number

  return sorted(y_sorted, key = lambda x: (x['line_number'], x['x']))

def teach_me_how_to_read(im):
  im = im.convert('RGB')
  start = time.time()

  all_letters = list(string.ascii_uppercase)
  results = []

  # TODO add this for the real thing for performance
  # , region=(300, 0, 500, 300)
  # , region=(300, 0, 500, 300)

  for key in all_letters:
    for hit in pyautogui.locateAll("keys/" + key + "_lower_key.png", im, confidence=0.96, grayscale=True):
      results.append({'capital': False, 'x': hit.left, 'y': hit.top, 'letter': key.lower(), 'width': hit.width, 'color': get_color(im, hit.left, hit.top, hit.width, hit.height)})
    for hit in pyautogui.locateAll("keys/" + key + "_upper_key.png", im, confidence=0.96, grayscale=True):
      results.append({'capital': True, 'x': hit.left, 'y': hit.top, 'letter': key, 'width': hit.width, 'color': get_color(im, hit.left, hit.top, hit.width, hit.height)})

  sorted_results = bucket(results)

  fully_baked_output = build_results(sorted_results)

  # TODO: Make togglable?
  # print_results(fully_baked_output)

  return fully_baked_output

