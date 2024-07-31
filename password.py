import random
import string

class PasswordGenerator:
    def __init__(self):
        self.password = ""

    def generate_password(self, length):
        if length < 6:
            raise ValueError("Password length should be at least 6 characters.")
        
        # Define the character pools
        lower_chars = string.ascii_lowercase
        upper_chars = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        
        # Ensure the password includes at least one of each type of character
        all_chars = lower_chars + upper_chars + digits + symbols
        self.password = (
            random.choice(lower_chars) +
            random.choice(upper_chars) +
            random.choice(digits) +
            random.choice(symbols) +
            ''.join(random.choices(all_chars, k=length - 4))
        )
        self.password = ''.join(random.sample(self.password, len(self.password)))  # Shuffle the password
        return self.password

    def display_password(self):
        if not self.password:
            print("No password generated yet.")
        else:
            print(f"Generated Password: {self.password}")

def main():
    generator = PasswordGenerator()

    while True:
        print("\nPassword Generator Menu")
        print("1. Generate Password")
        print("2. Display Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                length = int(input("Enter the length of the password (minimum 6 characters): "))
                password = generator.generate_password(length)
                print(f"Password generated: {password}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            generator.display_password()

        elif choice == '3':
            print("Exiting the password generator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
