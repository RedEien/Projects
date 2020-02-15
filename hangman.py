import random
from itertools import groupby
blank =[]

# chooses random word from list
def choose_word():
    with open('hangman.txt', 'r') as f:
        contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]

# gives blanks for the letters in the word ( kind of unnecessary)
def blank_word(word):
    global n
    for n in range(len(word)):
        n = n + 1

# checks if the input is in the word
def check_letter(word_letters, right_guesses, letter):
    # sorts out duplicates
    if letter in right_guesses:
        print('Du hast den Buchstaben '+letter+' schon einmal ausprobiert')
        return False
    # actual loop
    elif letter in word_letters:
        print(letter+' ist im Wort enthalten')
        right_guess = ''.join(k for k, g in groupby(sorted(guesses)))
        right_guesses.append(letter)
        return right_guesses
    else:
        print('falsch')
        return False

# checks if the word was found
def word_found(right_guesses, letter_list):
    if right_guesses == letter_list:
        print('Du hast das Wort erraten!')
        return True
    else:
        return False

def reveal_letters(letter, s_word, new_word):
    l = list(s_word)
    for i in range(len(s_word)):
        if letter == l[i]:
            new_word[i] = letter
            #print(new_word)
            i = i + 1
            continue
        else:
            continue
    print(new_word)

word = choose_word()
blank_word(word)
print('Willkommen bei Hangman. Versuch das Wort zu erraten, das sich hinter den _ versteckt')
new_word = ['_']*n
print(new_word)
# everything lower case
s_word = word.lower()
# gives a string of all letters in the word in alphabetical order
word_letters = ''.join(k for k, g in groupby(sorted(s_word)))
# writes all letters into a list
letter_list = list(word_letters)
# list of all guessed letters
guesses = []
#list of all right guessed letters
right_guesses = []

# loop for the guesses ends after word is guessed
while not word_found(right_guesses, letter_list):
    try:
        letter = str(input('Versuche einen Buchstaben zu erraten[a-z]: '))
        guesses.append(letter)
    except ValueError:
        continue  
    check_letter(word_letters, right_guesses, letter)   
    print('Folgende Buchstaben hast du schon ausprobiert: '+str(guesses))
    # kind of ugly reformation of the list in alphabetical order
    rights = ''.join(k for k, g in groupby(sorted(right_guesses)))
    right_guesses = list(rights)
    print('Diese Buchstaben hast du schon erraten: '+str(right_guesses))
    reveal_letters(letter, s_word, new_word)
