#!/usr/bin/python3

def python_snakes():
    try:
        num = int (input("put your number: "))
    except ValueError:
        print("Input a valid number please \n")
        python_snakes();
    else:
        space = ' '
        emoji = '😎'
        gap = num - 1
        for x in range(num):
            print(space * gap, emoji * x)
            gap -= 1


if __name__ == "__main__":
    python_snakes();