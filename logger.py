from datetime import datetime

def log(message, kind="main"):
  print(message)
  path = "logs/" + kind + ".txt"
  stamp = datetime.now().strftime("%m/%d/%Y | %H:%M:%S | ")
  try:
    f = open(path, "a")
    f.write(stamp + " " + message + "\n")
  finally:
    f.close()


def main():
  print("Test logger")

  log("Testing a lot")

if __name__ == "__main__":
  main()
