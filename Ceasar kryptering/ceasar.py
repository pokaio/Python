# Port of caesar fomr C to Python
# Program will only accept simple (and single) strings and no signs, e.g. exclamation marks etc.
# There's an easier method out there using .find & .replace functions


def main():
    # Prompt user for plaintext and key
    def user_input():
        plaintext = []
        key = []
        # Checks for valid plaintext-input
        while True:
            user_input.plaintext = input("Enter plaintext: ")
            # If input is 'empty'
            if not user_input.plaintext:
                print("Invalid plaintext")
            else:
                break
        # Checks for valid key-input
        while True:
            user_input.key = input("Enter key: ")
            # If no integer or invalid integer is entered
            if not user_input.key.isdigit() and int(user_input.key) < 0:
                print("Invalid number")
            else:
                break
    user_input()


    # Generate the ciphertext
    def ct():
        ct.ciphertext = ""
        for i in user_input.plaintext:
            if user_input.plaintext.istitle() or i.isspace():
                ct.ciphertext += chr((((ord(i) + int(user_input.key)) - 65) % 26) + 65)
            else:
                ct.ciphertext += chr((((ord(i) + int(user_input.key)) - 97) % 26) + 97)
    ct()

    print(
        "\n"
        "Plaintext entered:", user_input.plaintext, "\n"
        "Key entered: ", user_input.key, "\n"
        "Ciphertext: ", ct.ciphertext
        )


if __name__ == "__main__":
    main()
