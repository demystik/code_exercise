#!/usr/bin/python3

def Tup_of_std():
    """Your task is to write a code that
    will count how many males and females are in the list. Here is a
    list below:
    """
    students = ['Male', 'Female', 'female', 'male', 'male', 'male',
             'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
    males = [male for male in students if(male == "male" or male == "Male")]
    fmls = [fml for fml in students if(fml == "female" or fml == "Female")]
    numOfMale = len(males)
    numOfFemale = len(fmls)
    return [('Male', numOfMale),('female',numOfFemale)]

print(Tup_of_std())
