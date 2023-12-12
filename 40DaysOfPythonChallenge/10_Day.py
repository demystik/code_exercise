#!/usr/bin/python3

def hide_password():
    passwd = input("input password: ")
    return f"{'*'*len(passwd)}"

print(f"Your password is {len(hide_password())} characters")
