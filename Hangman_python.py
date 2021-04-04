## Hangman game
##Author: Maor Caspi
## Date: April 2021
## Note: Before running create "words.txt" with word in each new line.

import random
MAX_TRIES=6
HANGMAN_PHOTOS={
    "1":"    x-------x",
    "2":"""
    x-------x
    |
    |
    |
    |
    |
    """,
    "3":"""
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    "4": """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    "5": """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    "6":"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    "7":"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """}


HANGMAN_ASCII_ART=("  _    _                                         \n"
" | |  | |                                        \n"
" | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  \n"
" |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n"
" | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n"
" |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n"
"                      __/ |                      \n"
"                     |___/")

def try_update_letter_guessed(letter_guessed,old_letters_guessed):

##This function returns true if the letter_guessed string consists of only one char which is an English letter (and not another sign).

    if((len(letter_guessed)!=1 or not(letter_guessed>='a' and letter_guessed<='z')) or (letter_guessed in old_letters_guessed)):
        print("The input char is invalid")
        old_letters_guessed.sort()
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
    old_letters_guessed+=letter_guessed.lower()
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    hidden_word=secret_word
    hidden_word=hidden_word.replace("","_")
    hidden_word=hidden_word[::2]
    hidden_word=hidden_word.replace("_","_ ")
    hidden_word=hidden_word[:len(hidden_word)-2]
    for i in range(0,len(old_letters_guessed)):
        if(old_letters_guessed[i] in secret_word):
            position=secret_word.index(old_letters_guessed[i])
            temp=hidden_word
            hidden_word=temp[:position*2]+old_letters_guessed[i]+temp[position*2+1:]
    return(hidden_word)

def check_win(secret_word, old_letters_guessed):
    count=0;
    for i in range(0,len(old_letters_guessed)):
        if(old_letters_guessed[i] in secret_word):
            count+=count+1
    if(count==len(secret_word)):
        return True
    return False

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[str(num_of_tries)])

def choose_word():##return a random word from the text file
    f = open("words.txt", "r")
    text = f.readlines()
    f.close()
    f = open("words.txt", "r")
    index=random.randint(1,len(text))
    countOfLines=1
    for i in f:
        if(countOfLines==index):
            return(i)
            exit
        countOfLines=countOfLines+1
    f.close()


def main():
    print(HANGMAN_ASCII_ART)
    secret_word=(choose_word()).strip()##read a random word from the text file
    NumberOfSouls = 6
    sucssesCounter=0
    print_hangman(NumberOfSouls+1)
    old_letters = []##arrays of guessed letters
    lines=show_hidden_word(secret_word, old_letters)

    while(NumberOfSouls>1 and
         sucssesCounter!=len(secret_word)):
        isValidChar=False
        while(not isValidChar):
            tav=input("Guess a letter: ").lower()
            isValidChar=try_update_letter_guessed(tav,old_letters)
        newLines=show_hidden_word(secret_word, old_letters)
        print(newLines)
        if(lines==newLines):##if the curent guess was a bad guess
            NumberOfSouls=NumberOfSouls-1
            print("No..., now you have",NumberOfSouls,"souls")
            print_hangman(NumberOfSouls+1)
        else:
            sucssesCounter=sucssesCounter+1
        lines=newLines
        if(check_win(secret_word,old_letters)):
            break
    if(sucssesCounter==len(secret_word)):
        print("YOU WIN!!!")
    else:
        print("GAME OVER")

    
if __name__ == "__main__":
    main()
input()
