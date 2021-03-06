import re
import sys
import time

def build_regex(raw_string):
  wildcard = ".*"
  stripped_string = raw_string.strip()
  item_regex = ""
  lowers = "[a-z]"
  uppers = "[A-Z]"

  # All items should start with a capital. If ours doesn't, we missed the first letter
  if re.search(lowers, stripped_string[0]):
    item_regex = ".*"

  for i in range(len(stripped_string)):
    # If this is a space, and the next letter is lowercase, use a wildcard instead of a space.
    # Because we did string.strip() this won't ever look out of bounds.
    if stripped_string[i] == " " and re.search(lowers, stripped_string[i + 1]):
      item_regex += ".*"
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
    print("Direct hit!")
    return item_regex
  else:
    # No direct hit, and we could have missed the final letters, so end with wildcard
    item_regex = item_regex + ".*"
    items_string = "".join(item_names)
    print("RegEx searching: " + item_regex)
    search_result = re.findall(item_regex, items_string)
    if search_result and len(search_result) == 1:
      return search_result[0]
    elif not search_result:
      print("No matches.")
    else:
      print("Found multiple matches.")
      print(search_result)

  return "!!! Not Found !!!"

def main():
  start_time = time.time()
  if len(sys.argv) > 1:
    found_item = sys.argv[1]
  else:
    found_item = " une B w"
  print("\nBuilding regex for " + found_item)

  result = find_item(found_item)

  print("Result: " + result + ". Took " + str(round(time.time() - start_time, 3)) + " seconds.")
  return result

if __name__ == "__main__":
  main()



