#variables and open text file
f = open("hangman.txt", "r")
word = (f.read())
f.close()
wordlist = list(word)
guesslist = []
notinword = []
rightguess = 0
wrongguesses = 0
letterplace = 0
tilldeath = 6
loop = True

#import pics of hangman
from ggg import hangmanpics

for i in wordlist :

    guesslist.append("_")

#main code/tell user stuff
def main() :

    global loop
    global wrongguesses
    global letterguess

    while loop == True :

        loop = WinLose()
        print("You have already guessed")
        print(notinword)
        print("Your current info is")
        print(guesslist)
        letterguess = input("\nWhat character would you like to guess: ")
        CheckLetter()
        WrongRightInput()
        print("\nYou have " + str(tilldeath) + " more chances to get the word right")
        print("Or else Zion will get to your mom's house")
        print(hangmanpics[(wrongguesses)])

    if tilldeath == "0" :

        print("\nZion got to your mom's house!")
        LoseGame()

    else :

        print("\nYour mom is safe for now but Zion will be back soon")
        exit()

#check if user lost
def WinLose() :

    global loop
    global lose

    if tilldeath != 0 :

        loop = True
        return loop

    if "_" in guesslist :

        loop = True
        return loop

    else :

        loop = False

#check if inputed character is in word
def CheckLetter() :

    global letterguess
    global letterplace

    for i in wordlist :

        if letterguess == i :

            letterplace += 1
            guesslist.pop(letterplace)
            guesslist.insert(letterplace, letterguess)

#tell user if inputed character is character/right character
def WrongRightInput() :

    global tilldeath
    global letterguess
    global wrongguesses
    global wordlist
    global notinword

    if letterguess in wordlist :

        print("\nGood job this character is in the word")

    if len(letterguess) > 1 :

        print("\nYou broke the game!")
        exit()

    else :

        print("\nThis character is not in the word")
        notinword.append(letterguess)
        tilldeath -= 1
        wrongguesses += 1

#lose game stuff
def LoseGame() :

    zion = True
    zioncounter = 0

    while zion == True and zioncounter < 100 :

        print("RIP UR MOM")
        zioncounter += 1

main()

