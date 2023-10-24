def encode(password):
    digits = [int(digit) + 3 for digit in password]
    result = int(''.join(map(str, digits)))
    return result

def decode(encrypted):
    pass


if __name__ == '__main__':
    password = None
    encrypted = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif menu_option == 2:
            # Make the decode function where I defined it
            pass
        elif menu_option == 3:
            break
