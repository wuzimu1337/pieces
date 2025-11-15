import random

pwd = ""
char = int(input("Number of Characters:"))
num = 0
INT = [1,2,3,4,5,6,7,8,9,0]
STR = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
SPC = ["@","!","#","$","%","&"]
STr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

while num < char:
    part = random.choice(["INT","STR","SPC","STr"])
    if part == "INT":
        pwd += str(random.choice(INT))
        num += 1
    elif part == "STR":
        pwd += str(chr(random.choice(STR)+64))
        num += 1
    elif part == "SPC":
        pwd += str(random.choice(SPC))
        num += 1
    elif part == "STr":
        pwd += str(chr(random.choice(STr)+96))
        num += 1
    else:
        pass


print(f"Password:{pwd}")
