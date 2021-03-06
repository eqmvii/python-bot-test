# Class representing an item on the ground, read via OCR

class GroundItem:
  def __init__(self, letter):
    self.letters = [letter]
    self.color = letter["color"]
    self.line_number = letter["line_number"]

  def say_hi(self):
    print("Hi, my color is: " + color)

  def add_letter(self, letter):
    if letter["color"] != self.color:
      raise "I can't add a letter of a different color"
    if letter["line_number"] != self.line_number:
      raise "I can't add a letter on a different line"
    self.letters.append(letter)

  def name(self):
    return "".join(map(lambda letter: letter["letter"], self.letters))

  def last_letter(self):
    return self.letters[-1]

