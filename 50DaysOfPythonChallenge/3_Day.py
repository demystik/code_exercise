#!/usr/bin/python3
def register_check(register):
    presence = 0
    for val in register.values():
        if val == 'yes':
            presence += 1
    return presence

register = {'Michael':'yes','John': 'no','Peter':'yes', 'Mary': 'yes'}
print(register_check(register))
