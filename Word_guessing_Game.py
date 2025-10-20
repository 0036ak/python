import random

name=input("enter your name")
print("good luck ",name)
list=['rainbow','computer','science','programming','python',
      'vscode','laptop','house','market']
word=random.choice(list)
print('guess the characters')
guesses=''
turns=12
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end='')
        else:
            print('_')
            failed+=1
    if failed==0:
        print(" you win")
        print('the word is',word)
        break
    print()
    guess=input("guess a character:")
    guesses+=guess
    if guess not in word:
        turns-=1
        print('wrong')
        print("you have",+ turns,'more guesses')
        if turns==0:
         print('you loose')

