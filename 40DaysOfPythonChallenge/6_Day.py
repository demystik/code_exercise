#!/usr/bin/python3

def username():
    mail = input("mail: ")
    name, _ = mail.split('@')
    return name

print(username())
