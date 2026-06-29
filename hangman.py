import random

def choose_word():
    words = ["python", "hangman", "coding", "laptop", "keyboard"]
    return random.choice(words)

def display_board(wrong_guesses, guessed, guessed_wrong, word):
    print("\n" + "=" * 40)
    print(f"Wrong guesses left: {6 - wrong_guesses}")
    print(f"Wrong guesses: {', '.join(guessed_wrong) if guessed_wrong else 'None'}")
    
    display = []
    for letter in word:
        if letter in guessed:
            display.append(letter)
        else:
            display.append("_")
    print("Word: " + " ".join(display))
    print("=" * 40)
    return display

def hangman():
    word = choose_word()
    guessed = []
    guessed_wrong = []
    wrong_guesses = 0

    print("=" * 40)
    print("       Welcome to Hangman!")
    print("=" * 40)

    while wrong_guesses < 6:
        display = display_board(wrong_guesses, guessed, guessed_wrong, word)

        if "_" not in display:
            print(f"\n🎉 You win! The word was: {word}")
            break

        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!")
            continue

        if guess in guessed or guess in guessed_wrong:
            print("⚠️  You already guessed that letter!")
            continue

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word!")
            guessed.append(guess)
        else:
            print(f"❌ Wrong! '{guess}' is not in the word!")
            guessed_wrong.append(guess)
            wrong_guesses += 1

    if wrong_guesses == 6:
        print(f"\n💀 Game over! The word was: {word}")

hangman()