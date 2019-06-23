'''
The vigenere algorithm improves upon Caesar's encyption, using keywords
each letter in the keyword is assigned a value, a & A = 0, b & B = 1, etc.
The key wraps around itself once it's exhausted itself, i.e.
    Plaintext: abcd
    Key: ab = 01
    Translated: a+0, b+1, c+0, b+1 = a, c, c, e
'''
def main():
    # Prompt input from user
    def user_input():
        # Prompting the plaintext
        user_input.plaintext = ""
        while True:
            user_input.plaintext = "Hello, world!" #input("Plaintext: ")
            # Will accept anything except an 'empty' input
            if not user_input.plaintext:
                print("Invalid input")
            else:
                break
        # Prompting the key
        user_input.key = ""
        while True:
            user_input.key = "bcfk" #input("Key: ")
            # Will accepy everything, except 'empty' input
            if not user_input.key:
                print("Input key")
            else:
                break
    user_input()

    # Encrypting message
    # Converting the key into integers used to shift the plaintext
    def key():
        n = 0
        a = ""
        x = user_input.key
        key.i_key = ""
        for i in range(len(x)):
            a = ord(x[n])
            z = x[n]
            if z.islower():
                key.i_key += str(a - 97)
            else:
                key.i_key += str(a - 65)
            n += 1
    key()
    # Print ciphertext
    def ciphertext():
        shift = key.i_key
        n = 0
        a = ""
        ciphertext.b = ""
        x = user_input.plaintext
        y = user_input.key

        for i in range(len(x)):
            # Modulo
            mod = n % len(y)
            # Check for isalpha()
            z = x[n]
            # Checks for Capital and lower-case letters, all other symbols are pasted unmodified
            if z.islower():
                a = int(((ord(x[n]) + int(shift[mod]) - 97) % 26) + 97)
                ciphertext.b += chr(a)
            if z.istitle():
                a = int(((ord(x[n]) + int(shift[mod]) - 65) % 26) + 65)
                ciphertext.b += chr(a)
            # Check for anything that is not a letter. Add them directly to string b, e.g. space, exclamation mark, etc.
            if not z.isalpha():
                ciphertext.b += x[n]
            n += 1
    ciphertext()

    # Output
    print(
            "Plaintext:", user_input.plaintext, "\n"
            "Key:", user_input.key, "\n"
            "Converted key:", key.i_key, "\n"
            "Ciphertext:", ciphertext.b
        )
if __name__ == "__main__":
    main()
