#!/usr/bin/env python3

import random
import string

if __name__ == "__main__":
    def password():
        num = random.randrange(7, 11)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(num))
        print("My password is :", password)
    password()
