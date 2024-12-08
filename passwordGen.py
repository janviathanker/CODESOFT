import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    if length < 4:
        print("Password length should be at least 4 for a secure password.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for the password (minimum 4): "))
        password = generate_password(length)
        
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
