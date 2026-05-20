import random
import os

def clear_screen():
    # Clears the Windows command prompt screen for a clean UI
    os.system('cls')

def play_hangman():
    words = ["python", "coding", "windows", "script", "program"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    while attempts_left > 0:
        clear_screen()
        print("=== 🎮 WELCOME TO WINDOWS HANGMAN 🎮 ===")
        print(f"Attempts Remaining: {attempts_left}\n")

        # Display word progress
        display_word = "".join([letter if letter in guessed_letters else " _ " for letter in secret_word])
        print(f"Word: {display_word}\n")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")

        if " _ " not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            input("❌ Invalid input! Please enter a single letter. Press Enter...")
            continue

        if guess in guessed_letters:
            input("⚠️ You already guessed that letter! Press Enter...")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            input("✅ Good guess! Press Enter...")
        else:
            attempts_left -= 1
            input("❌ Wrong guess! Press Enter...")

    else:
        clear_screen()
        print("💀 GAME OVER! 💀")
        print(f"The secret word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()