import re
import sys
import time
import scroll_of_identify

def main():
  start_time = time.time()
  if len(sys.argv) > 1:
    found_item = sys.argv[1]
  else:
    found_item = " une B w"
  print("\nBuilding regex for " + found_item)

  result = scroll_of_identify.find_item(found_item)
  if result:
    print("Result: " + result + ". Took " + str(round(time.time() - start_time, 3)) + " seconds.")
  else:
    print("No Single Match")

  return result

if __name__ == "__main__":
  main()



