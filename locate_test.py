import pyautogui
import time
import string
import PIL
from PIL import Image

def print_results(sorted_letters):
  for line in range(sorted_letters[-1]['line_number']):
    # TODO ERIC ugh how to pipe where is my elixir
    line_letters = list(filter(lambda x: x['line_number'] == line, sorted_letters))
    # Start with a space, we have no capital letters yet
    spaced_letters = [" "]

    end_of_last_letter_x = line_letters[0]['x'] + line_letters[0]['width']
    for letter in line_letters:
      x_diff = letter['x'] - end_of_last_letter_x
      # TODO add more spaces if it's really big
      if x_diff > 7:
        spaced_letters.append(" ")
      end_of_last_letter_x = (letter['x'] + letter['width'])
      spaced_letters.append(letter["letter"])

    print("".join(spaced_letters))


# im = pyautogui.screenshot()

# sample_path = "samples/exotic_a1_letters.png"
# sample_path = "samples/exotic_cap_letters.png"
# sample_path = "samples/sample_items_screenshot.png"
# sample_path = "samples/L_cap_green.png"
# sample_path = "samples/random_new_sample.png"
# sample_path = "samples/inventory_dump.png"
# sample_path = "samples/3_charms.png"
sample_path = "samples/real_1.png"


im = Image.open(sample_path)
start = time.time()

all_letters = list(string.ascii_uppercase)

# Missing letters are giant yellow squares:
# Upper: X
# Lower: Q, Z
results = []

for key in all_letters:
  for o_hit in pyautogui.locateAll("keys/" + key + "_lower_key.png", im, region=(300, 0, 500, 300), confidence=0.95, grayscale=True):
    results.append({'x': o_hit.left, 'y': o_hit.top, 'letter': key, 'width': o_hit.width})
  for o_hit in pyautogui.locateAll("keys/" + key + "_upper_key.png", im, region=(380, 0, 500, 300), confidence=0.95, grayscale=True):
    results.append({'x': o_hit.left, 'y': o_hit.top, 'letter': key, 'width': o_hit.width})

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
#   print(letter['letter'] + "(" + str(letter['x']) + ", " + str(letter['y']) + ") - Line " + str(letter['line_number']))



print("Found " + str(len(multisorted)) + " letters\n\n")

print_results(multisorted)
print("\nBye now!\n")
print("Total run time: " + str(time.time() - start) + " seconds.")



