# try:
#   f = open("demofile2.txt", "a+")
#   a = f.readlines()
#   print(a)
#   f.write("walrus\n")
# finally:
#   f.close()


def write_items(new_items):
  # TODO ERIC: lol why am I opening to read, closing, then opening again to append?
  f_read = open("items.txt", "r")
  existing_items = f_read.readlines()
  f_read.close()

  f = open("items.txt", "a")

  unique_list = set(new_items)
  for new_item in new_items:
    if new_item + "\n" not in existing_items:
      f.write(new_item + "\n")

  f.close()

write_items(['hat', 'sock', "fork", "shoe", "ball", "big hat", "spoon"])

# f = open("items.txt")
# lines = f.readlines()
# for line in lines:
#     print(line)

