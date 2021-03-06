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

  results_tuple = scroll_of_identify.identify(found_item)
  print("Result: " + results_tuple[0] + ". Confidence: " + str(results_tuple[1]) + ". Took " + str(round(time.time() - start_time, 3)) + " seconds.")

  return results_tuple

if __name__ == "__main__":
  main()



