import string
import secrets


def random_password(length):
    letters = string.ascii_letters + string.digits + "@#$&*()+_{}-.=%"
    password = "".join(secrets.choice(letters) for i in range(length))
    return password


if __name__ == '__main__':
    password_Length = int(input("Enter the length of Password: "))
    print("Suggested Password:", random_password(password_Length))
