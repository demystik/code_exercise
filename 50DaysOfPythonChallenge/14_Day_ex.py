#!/usr/bin/python3

def your_salary():
    name = input("What is your name: ")
    numOfPeriod = int(input("How many times you teach this month: "))
    rate = input("What is your rate: ")
    overtime = (numOfPeriod - 100) * 25 if numOfPeriod > 100 else 0
    if numOfPeriod > 100:
        numOfPeriod = 100
    gross_salary = (numOfPeriod * 20) + overtime

    print(f"Teacher: {name}")
    print(f"Periods: {numOfPeriod + (overtime / 25):.0f}")
    print(f"Gross salary: {gross_salary:,}")

your_salary();