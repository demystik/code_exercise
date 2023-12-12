#!/usr/bin/python3

def dicOfNames():

    names = ["Joseph","Nathan", "Sasha", "Kelly",
             "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
    diff_name, dic = [], {}
    nam = [diff_name.append(name) for name in names if name not in diff_name and name[0] == "S"]
    for name in diff_name:
        num =  names.count(name)
        dic[name] = num
    print(dic)

dicOfNames()
