import random
from words import easy_word_list

def get_word():
    word = random.choice(easy_word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("\n🎮 Welcome to Emoji Hangman! 🎮\n")
    print(display_hangman(tries))
    print("Word to guess: " + word_completion)
    print("\n")

    while not guessed and tries > 0:
        print(f"❤️ Tries remaining: {tries}")
        print(f"🔠 Guessed letters: {' '.join(guessed_letters)}")
        print(f"❌ Incorrect words: {' '.join(guessed_words)}")
        print("-" * 50)

        guess = input("Please guess a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"\nYou already guessed the letter: {guess}")
            elif guess not in word:
                print(f"\nSorry, {guess} is not in the word. 😔")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"\nGreat job! {guess} is in the word! 🎉")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"\nYou already guessed the word: {guess}")
            elif guess != word:
                print(f"\n{guess} is not the word. 😕")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("\nInvalid input. Please enter a valid letter or word.")

        print(display_hangman(tries))
        print("Word to guess: " + word_completion)
        print("\n")

    if guessed:
        print(f"🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"😢 Sorry, you've run out of tries. The word was {word}.")
    
    play_again = input("\nWould you like to play again? (Y/N): ").upper()
    if play_again == 'Y':
        main()
    else:
        print("\nThanks for playing! Goodbye! 👋")

def display_hangman(tries):
    stages = [
        # Final state: head, torso, both arms, and both legs
        """
        --------
        |      |
        |     🙌🏽
        |     /\
        |
        --------
        """,
        # Head, torso, both arms, and one leg
        """
        --------
        |      |
        |     🙌🏽
        |     /
        |
        --------
        """,
        # Head, torso, and both arms
        """
        --------
        |      |
        |     🙌🏽
        | 
        |
        --------
        """,
        # Head, torso, and one arm
        """
        --------
        |      |
        |     🙋🏽
        | 
        |      
        |
        --------
        """,
        # Head and torso
        """
        --------
        |      |
        |      🙎
        |      
        |
        --------
        """,
        # Head
        """
        --------
        |      |
        |      🙍
        |
        |
        |
        --------
        """,
        # Initial empty state
        """
        --------
        |      |
        |
        |
        |
        --------
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
