import getpass

def simulate_login():
    print("--- Welcome to the Secure System ---")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    # Simulating a basic check
    if username == "admin" and password == "admin":
        print("\nLogin successful! Welcome, admin.")
    else:
        print("\nLogin failed. Invalid credentials.")

if __name__ == "__main__":
    simulate_login()