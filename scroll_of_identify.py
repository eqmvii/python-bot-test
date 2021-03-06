import re
import sys
import time
import logger

common_misses = {
  'Gold': 'Gold',
  'old': 'Gold',
  'Go d': 'Gold',
  'G ld': 'Gold',
  'Gol': 'Gold',
  'Key': 'Key',
  'Ke': 'Key',
  'ey': 'Key',
  # Reading life from bottom left of the screen
  'ife': 'Life',
  'Life': 'Life'
  }

def build_regex(stripped_string):
  wildcard = ".*"
  item_regex = ""
  lowers = "[a-z]"

  # All items should start with a capital. If ours doesn't, we missed the first letter
  if re.search(lowers, stripped_string[0]):
    item_regex = wildcard

  for i in range(len(stripped_string)):
    # If this is a space, and the next letter is lowercase, use a wildcard instead of a space.
    # Because we did string.strip() this won't ever look out of bounds.
    if stripped_string[i] == " " and re.search(lowers, stripped_string[i + 1]):
      item_regex += wildcard
    else:
      item_regex += stripped_string[i]

  return item_regex


def find_item(raw_found_item_string, items_filename="item_names.txt"):
  item_regex = build_regex(raw_found_item_string)

  try:
    f = open(items_filename, "r")
    item_names = f.readlines()
  finally:
    f.close()

  if item_regex + "\n" in item_names:
    return item_regex
  else:
    # No direct hit, and we could have missed the final letters, so end with wildcard
    item_regex = item_regex + ".*"
    items_string = "".join(item_names)
    search_result = re.findall(item_regex, items_string)
    if search_result and len(search_result) == 1:
      return search_result[0]
    elif not search_result:
      logger.log("No results for " + raw_found_item_string + ", as: " + item_regex, "item_id")
    else:
      logger.log("Multiple results for " + raw_found_item_string + ", as: " + item_regex, "item_id")

  return None

def identify(raw_item_text):
  confidence = 0
  input_string = raw_item_text.strip()

  if input_string in common_misses:
    confidence = 1
    result = common_misses[input_string]
  else:
    result = find_item(input_string)
    if result:
      confidence = 1
    else:
      result = raw_item_text

  return (result, confidence)
