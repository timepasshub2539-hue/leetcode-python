import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def get_secret_num():
    digits = list("0123456789")
    return "".join(random.sample(digits, NUM_DIGITS))


def get_clues(guess, secret):
    if guess == secret:
        return "You got it!"
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues.append("Fermi")
        elif guess[i] in secret:
            clues.append("Pico")
    if not clues:
        return "Bagels"
    clues.sort()
    return " ".join(clues)


def main():
    while True:
        secret = get_secret_num()
        print(f"I'm thinking of a {NUM_DIGITS}-digit number.")
        guesses = 1
        while guesses <= MAX_GUESSES:
            guess = input(f"Guess {guesses}: ")
            print(get_clues(guess, secret))
            if guess == secret:
                break
            guesses += 1
        else:
            print(f"Out of guesses. It was {secret}.")
        if not input("Play again? (y/n) ").lower().startswith("y"):
            break


if __name__ == "__main__":
    main()
