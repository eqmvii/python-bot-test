tc_87 = [
  "Giant Thresher",
  "Mythical Sword",
  "Caduceus",
  "Vortex Shield",
  "Corona",
  "Sacred Armor",
  "Thunder Maul",
  "Scissors Suwayyah",
  "Hydra Bow",
  "Colossus Blade",
  "Diadem",
  "Shadow Plate",
  "Ogre Gauntlets",
  "Berserker Axe",
  "Glorious Axe",
  "Legend Spike",
  "Winged Harpoon",
  "War Pike",
  "Archon Staff",
  "Unearthed Wand",
  "Dimensional Shard",
  "Bloodlord Skull",
  "Myrmidon Greaves"
]

valuable = [
  "Monarch",
  "Shako",
  "Jewel",
  "Ring",
  "Amulet",
  "Dusk Shroud"
]

missing = [
  "Grand Crown",
  "Armet",
  "Spired Helm",
  "Kraken Shell",
  "Shadow Plate",
  "Tigulated Mail",
  "Chaos Armor",
  "Troll Nest",
  "Ward",
  "Dragon Shield",
  "Battle Gauntlets",
  "War Spike",
  "Champion Axe",
  "Twin Axe",
  "Crusader Bow",
  "Ghost Glaive",
  "Legendary Mallet",
  "Cryptic Axe",
  "Mighty Scepter",
  "Battle Scythe",
  "Holy Water Sprinkler",
  "Elegant Blade",
  "Jo Staff",
  "Gothic Staff",
  "Rune Staff",
  "Lich Wand",
  "Unearthed Wand",
  "Tomb Wand",
  "Ceremonial Pike",
  "Earth Spirit",
  "Sky Spirit",
  "Bloodlord Skull",
  "Zakarum Shield"
]

other = [
  "Balrog Skin"
]

common_misses = {
  'Reijuvenation Potion': "Rejuvination Potion"
}

def identify(raw_item_text):
  confidence = 0
  identity = raw_item_text.strip()

  desired_items = tc_87 + valuable + missing + other
  if raw_item_text in desired_items:
    confidence = 1
  elif raw_item_text in common_misses:
    confidence = 1
    identity = common_misses[raw_item_text]
  # TODO: RegEx "crossword" solver

  if confidence > 0.9:
    print("High Confidence Find: " + identity)

  return (raw_item_text, confidence)
