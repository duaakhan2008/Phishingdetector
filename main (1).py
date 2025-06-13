import string
import random
import re

def check_strength(password):
    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_number = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([has_upper, has_lower, has_number, has_symbol])

    if length < 6:
        return "Very Weak ❌"
    elif score == 4 and length >= 12:
        return "Strong 💪"
    elif score >= 3:
        return "Moderate 👍"
    else:
        return "Weak ⚠️"

def generate_password(length=12):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

print("🔐 Welcome to the Password Strength Tester + Generator!")

while True:
    print("\nChoose an option:")
    print("1: Check a password")
    print("2: Generate a strong password")
    print("3: Exit")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        user_password = input("Type your password: ")
        strength = check_strength(user_password)
        print("Your password is:", strength)

    elif choice == "2":
        length = int(input("How long should your password be? "))
        new_pass = generate_password(length)
        print("Here’s your strong password:", new_pass)

    elif choice == "3":
        print("Goodbye! Stay safe online. 🛡️")
        break

    else:
        print("Oops! Please enter 1, 2, or 3.")
