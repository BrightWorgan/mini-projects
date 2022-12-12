# Edle Idea
# Educational Wordle
#
#
# take input from user
# remove common words like and, as, then, etc.
# store remaining words in a list or dictionary
# choose a word at random
# print out a underscore for everty letter in the randomaly choosesn word , i.e. "_"
# ask user to enter a guess
# if guess letter is in the random word replace the corospoding _ with the guessed letter, update "current word" and print out 
#  ( i.e. is the word was ancient and only the letter n was guessed correctly =  _ n _ _ _ e t )
# if the guess is not in the word print a "try agian message"

# store of negative responses
# strore of positive responsces
# store of words
# current word


# list of words to be removed
RemovalWords = []

# play = "n"
# get user input
play = input("\tHello there. Do you wish to play a game? \n\t Y/N?").lower()
# while loop
while play != "y":
# get user input
    # play = input("\tHello there. Do you wish to play a game? \n\t Y/N?").lower()
    # check user's answer
    if play == "y":
        print("\tFantastic! The let's get started")
    elif play == "n":
        print("\tMaybe another time.")
    else: 
        print("\t ERROR: Please enter Y or N")

# get user's paragraph
paragraph = input("\tPlease enter the paragraph you wish to Edle today! ")

# list of word
booklet = list.spilt(paragraph)
print(booklet)
# remove "and" words
for word in len(booklet):
    if word  in RemovalWords:
        booklet.remove(word)


