#!/usr/bin/python3
def age_in_minutes():
    age = input("Your year of birth: ")
    if int(age) > 2023 or int(age) < 1900:
        print("!! invalid age: ", age)
        age_in_minutes()
    if len(age) != 4:
        print("!! Put a 4 digits number")
        age_in_minutes()
    return ((((2022 - int(age)) * 12) * 365) * 12) * 12


print(f"You are {age_in_minutes():,} minutes old")
