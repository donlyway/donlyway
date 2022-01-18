#list of letters and points for scrabble
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#merge both lists into a dictonary titled letter_to_points
letter_to_points =  {
key: value
for key, value
in zip(letters, points)
}
#add a blank space with value of 0
letter_to_points[" "] = 0
print(letter_to_points)

#create a function that will determine the score of the word
def score_word(word):
  point_total = 0
  #fadd the point total for every letter in the word
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

#test the score of the word Brownie  
brownie_points = score_word("BROWNIE")
print(brownie_points)

#create a score board of each player and their associated words
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con" : ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "Coma", "PERIOD"]}
player_to_points = {}

#determin the score of each player
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)
