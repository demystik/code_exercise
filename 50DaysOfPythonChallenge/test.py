#!/usr/bin/python3
names = ["kerry", "dickson","ade","sola","ade","sola","John", "Mary","carol", "Rose", "adam"]
seg_name = []
seg_nam = [seg_name.append(name) for name in names if name not in seg_name]
#for name in names:
#    if name not in seg_name:
#        seg_name.append(name)
print(seg_name)
