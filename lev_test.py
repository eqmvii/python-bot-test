
from Levenshtein import distance as levenshtein_distance

print("hullo")

finds = [
  "LL iant Thre her",
  "Breast Plate",
  "Lance",
  "Axe",
  "Ward Bow",
  "Russet Armor"
]

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

targets = tc_87 + valuable + missing

# hmmm not sure what direction to go from here
for find in finds:
  for target in targets:
    if len(target) <= 4:
      max_distance = 2
    elif len(target) == 5:
      max_distance = 3
    else:
      max_distance = 4

    if levenshtein_distance(find, target) <= max_distance:
      print(find + " could be " + target + "?")
