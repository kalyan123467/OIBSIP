"""
Random Password Generator
Generates passwords using uppercase, lowercase, digits, and symbols.
"""

import random
import string


def generate_password(length):
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    for _ in range(length - 4):
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)


def main():
    print("=== Random Password Generator ===")

    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Length must be at least 4.")
            return

        password = generate_password(length)
        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
