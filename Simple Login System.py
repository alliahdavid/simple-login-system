import getpass
# Predefined credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

while True:
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()

    if username.lower() == VALID_USERNAME and password == VALID_PASSWORD:
        print("Access Granted")
        break
    else:
        print("Access Denied. Please Try Again.\n")