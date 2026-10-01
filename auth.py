from config import TEACHERS
from UI import banner

def login():
    banner(" TEACHER'S LOG IN ")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if TEACHERS.get(username) == password:
        print(f"\nWelcome, {username}!")
        return True
    print("\nInvalid Username or password.\n")
    return False