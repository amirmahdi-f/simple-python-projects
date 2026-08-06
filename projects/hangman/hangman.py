from hangman_art import stages
import random


word_list = [
"abruptly", 
"absurd", 
"abyss", 
"affix", 
"askew", 
"avenue", 
"awkward", 
"axiom", 
"azure", 
"bagpipes", 
"bandwagon", 
"banjo", 
"bayou", 
"beekeeper", 
"bikini", 
"blitz", 
"blizzard", 
"boggle", 
"bookworm", 
"boxcar", 
"boxful", 
"buckaroo", 
"buffalo", 
"buffoon", 
"buxom", 
"buzzard", 
"buzzing", 
"buzzwords", 
"caliph", 
"cobweb", 
"cockiness", 
"croquet", 
"crypt", 
"curacao", 
"cycle", 
"daiquiri", 
"dirndl", 
"disavow", 
"dizzying", 
"duplex", 
"dwarves", 
"embezzle", 
"equip", 
"espionage", 
"euouae", 
"exodus", 
"faking", 
"fishhook", 
"fixable", 
"fjord", 
"flapjack", 
"flopping", 
"fluffiness", 
"flyby", 
"foxglove", 
"frazzled", 
"frizzled", 
"fuchsia", 
"funny", 
"gabby", 
"galaxy", 
"galvanize", 
"gazebo", 
"giaour", 
"gizmo", 
"glowworm", 
"glyph", 
"gnarly", 
"gnostic", 
"gossip", 
"grogginess", 
"haiku", 
"haphazard", 
"hyphen", 
"iatrogenic", 
"icebox", 
"injury", 
"ivory", 
"ivy", 
"jackpot", 
"jaundice", 
"jawbreaker", 
"jaywalk", 
"jazziest", 
"jazzy", 
"jelly", 
"jigsaw", 
"jinx", 
"jiujitsu", 
"jockey", 
"jogging", 
"joking", 
"jovial", 
"joyful", 
"juicy", 
"jukebox", 
"jumbo", 
"kayak", 
"kazoo", 
"keyhole", 
"khaki", 
"kilobyte", 
"kiosk", 
"kitsch", 
"kiwifruit", 
"klutz", 
"knapsack", 
"larynx", 
"lengths", 
"lucky", 
"luxury", 
"lymph", 
"marquis", 
"matrix", 
"megahertz", 
"microwave", 
"mnemonic", 
"mystify", 
"naphtha", 
"nightclub", 
"nowadays", 
"numbskull", 
"nymph", 
"onyx", 
"ovary", 
"oxidize", 
"oxygen", 
"pajama", 
"peekaboo", 
"phlegm", 
"pixel", 
"pizazz", 
"pneumonia", 
"polka", 
"pshaw", 
"psyche", 
"puppy", 
"puzzling", 
"quartz", 
"queue", 
"quips", 
"quixotic", 
"quiz", 
"quizzes", 
"quorum", 
"razzmatazz", 
"rhubarb", 
"rhythm", 
"rickshaw", 
"schnapps", 
"scratch", 
"shiv", 
"snazzy", 
"sphinx", 
"spritz", 
"squawk", 
"staff", 
"strength", 
"strengths", 
"stretch", 
"stronghold", 
"stymied", 
"subway", 
"swivel", 
"syndrome", 
"thriftless", 
"thumbscrew", 
"topaz", 
"transcript", 
"transgress", 
"transplant", 
"triphthong", 
"twelfth", 
"twelfths", 
"unknown", 
"unworthy", 
"unzip", 
"uptown", 
"vaporize", 
"vixen", 
"vodka", 
"voodoo", 
"vortex", 
"voyeurism", 
"walkway", 
"waltz", 
"wave", 
"wavy", 
"waxy", 
"wellspring", 
"wheezy", 
"whiskey", 
"whizzing", 
"whomever", 
"wimpy", 
"witchcraft", 
"wizard", 
"woozy", 
"wristwatch", 
"wyvern", 
"xylophone", 
"yachtsman", 
"yippee", 
"yoked", 
"youthful", 
"yummy", 
"zephyr", 
"zigzag", 
"zigzagging", 
"zilch", 
"zipper", 
"zodiac", 
"zombie", 
]

def get_word(word_list):
  return random.choice(word_list)

def under_line(text, solved_word_list):
  under_line_txt = ''
  for word in text:
    if word in solved_word_list:
      under_line_txt+= word
    else:
      under_line_txt += "_"
  return under_line_txt

def check_win(text, word):
    if "_" not in text:
        print(f"🎉 You won! The word is '{word}'")
        return True

def show_hangman (wrong_count):
  if wrong_count <= len(stages):
    return stages[-(wrong_count+1)]

word = get_word(word_list)
solved_words = []
wrong_guess = 0
max_wrong = 6

win = False

#game_loop
while wrong_guess < max_wrong:
  print(under_line(word, solved_words))
  user_word = input("enter you guess letter : ")
  print(f'wrong guesses : {wrong_guess}')

  if not user_word.isalpha() or len(user_word) != 1:
    print("just enter a single letter : ")

  elif user_word in solved_words:
    print("dont use repetitive word's")

  elif user_word not in word:
    print(f"{user_word} not in word")
    wrong_guess += 1
    print(show_hangman(wrong_guess))

  else:
    print(f"{user_word} in word")
    solved_words.append(user_word)
    print(show_hangman(wrong_guess))

  if check_win(under_line(word, solved_words), word):
    print(f"you won word is : {word}")
    win = True
    break

if not win :  
  print(f"oops!! right word is {word}")