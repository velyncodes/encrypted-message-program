from random import randint
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def generate_otp(sheets, length):
    for sheet in range(sheets):
        with open(f"otps{str(sheet)}.txt", "w") as f:
            for i in range(length):
                f.write(f"{str(randint(0, 26))}\n")


def load_sheet(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents


def get_plaintext():
    plaintext = input("Please type your message: ")
    return plaintext.lower()


def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents


def save_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)


def encrypt(plaintext, sheet):
    ciphertext = ""
    for position, char in enumerate(plaintext):
        if char not in alphabet:
            ciphertext += char
        else:
            encrypted = (alphabet.index(char) + int(sheet[position])) % 26
            ciphertext += alphabet[encrypted]
    return ciphertext


def decrypt(ciphertext, sheet):
    plaintext = ''
    for position, char in enumerate(ciphertext):
        if char not in alphabet:
            plaintext += char
        else:
            decrypted = (alphabet.index(char) - int(sheet[position])) % 26
            plaintext += alphabet[decrypted]
    return plaintext


def menu():
    choices = ['1', '2', '3', '4']
    choice = '0'
    while True:
        while choice not in choices:
            print('What would you like to do?')
            print('1. Generate one-time pads')
            print('2. Encrypt a message')
            print('3. Decrypt a message')
            print('4. Quit the program')
            choice = input('Please type 1, 2, 3 or 4 and press Enter: ')
            if choice == '1':
                sheets = int(
                    input('How many one-time pads would you like to generate? '))
                length = int(
                    input('What will be your maximum message length? '))
                generate_otp(sheets, length)
            elif choice == '2':
                filename = input(
                    'Type in the filename of the OTP you want to use ')
                sheet = load_sheet(filename)
                plaintext = get_plaintext()
                ciphertext = encrypt(plaintext, sheet)
                filename = input(
                    'What will be the name of the encrypted file? ')
                save_file(filename, ciphertext)
            elif choice == '3':
                filename = input(
                    'Type in the filename of the OTP you want to use ')
                sheet = load_sheet(filename)
                filename = input(
                    'Type in the name of the file to be decrypted ')
                ciphertext = load_file(filename)
                plaintext = decrypt(ciphertext, sheet)
                print('The message reads:')
                print('')
                print(plaintext)
            elif choice == '4':
                exit()
            choice = '0'


# generate_otp(5, 100)
menu()
