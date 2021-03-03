import pyautogui
import time
import PIL
from PIL import Image

# im = pyautogui.screenshot()

sample_path = "samples/sample_items_screenshot.png"

im = Image.open(sample_path)
start = time.time()

letters = ['O', 'I', 'T', 'N']
results = []

lower_a_hits = pyautogui.locateAll("keys/A_lower_key.png", im, confidence=0.9, grayscale=True)

for key in letters:
  for o_hit in pyautogui.locateAll("keys/" + key + "_lower_key.png", im, confidence=0.95, grayscale=True):
    results.append({'x': o_hit.left, 'y': o_hit.top, 'letter': key})

# lower_i_hits = pyautogui.locateAll("keys/I_lower_key.png", im, confidence=0.9, grayscale=True)
# lower_t_hits = pyautogui.locateAll("keys/T_lower_key.png", im, confidence=0.9, grayscale=True)
# lower_n_hits = pyautogui.locateAll("keys/N_lower_key.png", im, confidence=0.9, grayscale=True)


# Lines are 16 pixels tall

# Add ~5 pixels to our smallest lower case and go from there

print("Took " + str(time.time() - start) + " seconds.")

# sorted_y = sorted(results, key=lambda letter: letter['y'])

multisorted = sorted(results, key = lambda x: (x['y'], x['x']))

for letter in multisorted:
  print(letter['letter'] + "(" + str(letter['x']) + ", " + str(letter['y']) + ")")

print("Found " + str(len(multisorted)) + " letters")



