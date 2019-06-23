# Crack passwords
''' https://www.youtube.com/watch?v=--tnZMuoK3E
A hash is a one-way encryption, in that we are unable to revert back to the original pwd from the hash.
Every website/program etc. will save the hashes instead of the user's psw, so that in case they get hacked
they'll only expose the generated hashes. However, there are 'raibowtable' out there with 4b hashes
that will easily recognize the most common pwds. To counter 'rainbow-tables' most algorithms include salt, which is a
random string added to the pwd, and stored as plaintext along the hash so that the program knows which salt
to use next time. E.g.
    Pwd: "hey"
    salt: 7#!
    Pwd used to generate hash: hey7#!
The way a website will recognize the user and its pwd is by generating a new hash (including the salt) and compare
it to the hash already stored on the server.
'''
# Used to generate DES-method algorithm encrpytion
import crypt
# Used in sha256 encrpytion
import hashlib
import random

from string import ascii_letters
# Permutation tools. Tools to compute the permuations and combinations
import itertools
'''
A more secure encryption is using sha256 method
m = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
m = hashlib.sha256("hello".encode('utf-8')).hexdigest()
'''

# Condition: upto 4 characters long, only letters (upper and/or lowercase)
# 1. Get hashed password, DES-based algorithm, two parameters: 1. pwd & 2. salt, i.e. key

pwd = "aaaa"
salt = "50"
hashed = crypt.crypt(pwd, salt)

# 2. Crack hashed password
# The letters we want to permuate to generate possible passwords
string = ascii_letters

# Where we will store the generated hash to compare against the hashed pwd
comp = ""
# Integer used in itertools
rep = 1
while True:
    # The itertools is used to create all possible combinations
    for i in itertools.product(string, repeat = rep):
        s = str(''.join(i))
        comp = crypt.crypt(s, salt)
        # The print is used for debugging purposes
        # print(s, comp)
        if hashed == comp:
            break
    # This print is used for debugging purposes as well
    print()
    # Increase the permutation of strings length i++
    rep += 1

    if hashed == comp:
        print(
            "Hashed pwd:", hashed, "\n"
            "Calculated:", comp, "\n"
            "Password:", s
            )
        break
