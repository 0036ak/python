import random
from collections import Counter

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print("Guess the word — hint: 'It is a fruit name'")
    print("letter in word ",len(word))
    print('_ ' * len(word))  # print underscores for the word

    letterguessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while chances != 0:
            print()
            guess = input("Enter a letter to guess: ").lower()

            if not guess.isalpha():
                print("Enter only alphabet letters!")
                continue
            elif len(guess) > 1:
                print("Enter a single letter only!")
                continue
            elif guess in letterguessed:
                print("You already guessed that letter.")
                continue

            # Add guess to guessed letters
            letterguessed += guess

            if guess in word:
                print(f"Good guess! '{guess}' is in the word.")
            else:
                print(f"Oops! '{guess}' is not in the word.")
                chances -= 1

            # Display current progress
            correct_letters = 0
            for char in word:
                if char in letterguessed:
                    print(char, end=" ")
                    correct_letters += 1
                else:
                    print("_", end=" ")

            print(f"\nChances left: {chances}")

            # Win check
            if correct_letters == len(word):
                print("\nCongratulations! You guessed the word:", word)
                flag = 1
                break

        if flag == 0:
            print("\nYou lost! The word was:", word)

    except KeyboardInterrupt:
        print("\n\nGame interrupted. Bye!")
