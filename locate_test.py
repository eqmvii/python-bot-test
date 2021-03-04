import pyautogui
import time
import string
import PIL
from PIL import Image

def print_results(sorted_letters):
  for line in range(sorted_letters[-1]['line_number']):
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



# im = pyautogui.screenshot()

# sample_path = "samples/exotic_a1_letters.png"
# sample_path = "samples/exotic_cap_letters.png"
# sample_path = "samples/sample_items_screenshot.png"
# sample_path = "samples/L_cap_green.png"
# sample_path = "samples/random_new_sample.png"
# sample_path = "samples/inventory_dump.png"
# sample_path = "samples/3_charms.png"
# sample_path = "samples/real_1.png"
# sample_path = "run_screens/1614816938.44777_run_shot.png"
# sample_path = "run_screens/1614816964.662444_run_shot.png"
# sample_path = "run_screens/1614817675.8922539_run_shot.png"

sample_path = "run_screens/set_1614826686.6638985_run_shot.png"


im = Image.open(sample_path)
im = im.convert('RGB')
start = time.time()

all_letters = list(string.ascii_uppercase)

# Missing letters are giant yellow squares:
# Upper: X
# Lower: Q, Z
results = []

# TODO add this for the real thing for performance
# , region=(300, 0, 500, 300)
# , region=(300, 0, 500, 300)

for key in all_letters:
  for hit in pyautogui.locateAll("keys/" + key + "_lower_key.png", im, confidence=0.96, grayscale=True):
    results.append({'x': hit.left, 'y': hit.top, 'letter': key, 'width': hit.width, 'color': get_color(im, hit.left, hit.top, hit.width, hit.height)})
  for hit in pyautogui.locateAll("keys/" + key + "_upper_key.png", im, confidence=0.96, grayscale=True):
    results.append({'x': hit.left, 'y': hit.top, 'letter': key, 'width': hit.width, 'color': get_color(im, hit.left, hit.top, hit.width, hit.height)})

# Lines are 16 pixels tall

# Add ~5 pixels to our smallest lower case and go from there

# TODO ERIC -- line sort
# 1. find lowest y
# 2. Add all Ys that are within 6 pixels
# 3. Repeat until everything is in a line

print("Picture Hunting took " + str(time.time() - start) + " seconds.")

# sorted_y = sorted(results, key=lambda letter: letter['y'])

# multisorted = sorted(results, key = lambda x: (x['y'], x['x']))

print("Bucket Time")
y_sorted = sorted(results, key=lambda letter: letter['y'])

current_line_number = 0
current_row_y = y_sorted[0]['y']
for letter in y_sorted:
  if letter['y'] - current_row_y <= 7:
    letter['line_number'] = current_line_number
  else:
    current_line_number += 1
    current_row_y = letter['y']
    letter['line_number'] = current_line_number

# line_sorted = sorted(results, key=lambda letter: letter['line_number'])
multisorted = sorted(results, key = lambda x: (x['line_number'], x['x']))

print("Picture Hunting + line bucketing took " + str(time.time() - start) + " seconds.")

# for letter in multisorted:
#   print(letter['letter'] + "(" + str(letter['x']) + ", " + str(letter['y']) + ") - Line " + str(letter['line_number']) + " color: " + letter['color'])

# TODO: Add Levenshtein Distance

print("Found " + str(len(multisorted)) + " letters\n\n")

print(sample_path + "\n")
print_results(multisorted)
print("\nBye now!\n")
print("Total run time: " + str(time.time() - start) + " seconds.")
print(im.mode)

