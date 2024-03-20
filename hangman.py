#HANGMAN PROJECT
import random
words = ['computer','python','information','world','study','maths','science',
         'english','hindi','sst','society','between','intelligent','country',
         'fabulous','galaxy','planets','stars']

name=str(input("ENTER YOUR NAME:"))
print("BEST OF LUCK", name)
word=random.choice(words)
guesses=str(input("GUESS THE ALPHABETS:"))
moves=10
while moves>0:
    fail=0
    for i in word:
        if i in guesses:
            print(i)
        else:
            print("_")
            fail+=1
    if fail==0:
        print("YOU WIN")
        print("THE WORD IS",word)
        break
    guess=str(input("GUESS THE ALPHABET:"))
    guesses+=guess
    if guess not in word:
        moves-=1
        print("WRONG")
        print("YOU HAVE", moves,"MORE GUESSES")
        if moves==0:
            print("YOU LOOSE")
