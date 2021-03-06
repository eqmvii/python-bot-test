import re
import sys
import time
import logger

common_misses = {
  # Important things - these are near certain, but have lots of RegEx matches otherwise
  'ing': 'Ring',
  'R ng': 'Ring',
  'Rin': 'Ring',
  # BS
  'Gold Gold': 'Gold (but twice lol)',
  'Gold': 'Gold',
  'old': 'Gold',
  'Go d': 'Gold',
  'G ld': 'Gold',
  'Gol': 'Gold',
  'Key': 'Key',
  'Ke': 'Key',
  'ey': 'Key',
  'Full Reijuvenation Potion': 'Full Rejuvination Potion',
  'Reijuvenation Potion': 'Rejuvination Potion',
  # Reading life from bottom left of the screen
  'ife': 'Life',
  'Life': 'Life'
  }

def build_regex(stripped_string):
  wildcard = ".*"
  lowers = "[a-z]"

  # All items should start with a capital. If ours doesn't, we missed the first letter
  if re.search(lowers, stripped_string[0]):
    item_regex = wildcard
  else:
    # Small hack, we're searching one string, so a new word means the end of the last string.
    # Be sure file has a new line at the start.
    item_regex = "\n"

  for i in range(len(stripped_string)):
    # To match Wa Hammer, need to make all spaces wild cards :/
    if stripped_string[i] == " ":
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

  # lstrip hack needed since we add the \n above... should clean this up...
  if item_regex.lstrip() + "\n" in item_names:
    return item_regex
  else:
    # No direct hit, and we could have missed the final letters, so end with wildcard
    item_regex = item_regex + ".*"
    items_string = "".join(item_names)
    search_result = re.findall(item_regex, items_string)
    if search_result and len(search_result) == 1:
      return search_result[0]
    elif not search_result:
      logger.log("No results for " + raw_found_item_string + ", as: " + item_regex.lstrip(), "item_id")
    else:
      # TODO: Somehow save these, so possible IDs for things like charms and jewels can get picked
      logger.log(str(len(search_result)) + " results for " + raw_found_item_string + ". Used '" + item_regex.lstrip() + "' as RegEx.", "item_id")
      # logger.log("[" + "| ".join("".join(search_result).split("\n")) + " ]", "item_id")

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

  return (result.lstrip(), confidence)
