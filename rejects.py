def list_items():
  try:
    f = open("reject.txt", "r")
    items_to_reject = f.readlines()
  finally:
    f.close()

  return items_to_reject


def main():
  print("Test Reject")

  print(list_items())

if __name__ == "__main__":
  main()
