import random
import string

def generate_password(length=12, include_symbols=True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if include_symbols else ""
    all_chars = letters + digits + symbols

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]
    if include_symbols:
        password.append(random.choice(string.punctuation))

    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    print("🔐 Strong Password Generator 🔐")
    try:
        length = int(input("Enter desired password length (default 12): ") or 12)
        include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, include_symbols)
        print(f"\n✅ Your generated password: {password}")
    except ValueError:
        print("❌ Invalid input! Please enter a number for length.")
