# Class representing an item on the ground, read via OCR
import scroll_of_identify

class GroundItem:
  def __init__(self, letter):
    self.letters = [letter]
    self.color = letter["color"]
    self.line_number = letter["line_number"]
    self.identity = "!!! UNIDENTIFIED !!!"
    self.confidence = 0

  def say_hi(self):
    print("Hi, my color is: " + color)

  def add_letter(self, letter):
    if letter["color"] != self.color:
      raise "I can't add a letter of a different color"
    if letter["line_number"] != self.line_number:
      raise "I can't add a letter on a different line"
    self.letters.append(letter)

  def full_name(self):
    if self.confidence == 1:
      return "(" + self.color + ") " + self.identity
    else:
      return "(" + self.color + ") " + self.name() + " [Failed To Identify]"

  def name(self):
    return "".join(map(lambda letter: letter["letter"], self.letters))

  def last_letter(self):
    return self.letters[-1]

  def pickup_x(self):
    return self.letters[0]["x"] + 2

  def pickup_y(self):
    return self.letters[0]["y"] + 2

  def has_interesting_color(self):
    return self.color == "green" or self.color == "gold" or self.color == "red"

  def identify(self):
    id_tuple = scroll_of_identify.identify(self.name())
    self.identity = id_tuple[0]
    self.confidence = id_tuple[1]

