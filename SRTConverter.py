import sys

symbols = ["-", "," , ">", ":", "#", "="]
numeric = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

userfile = sys.argv[1]
newfile = userfile + "-converted.txt"

userfile = open(userfile, "r")
new = open(newfile, "w")
count = 0

while True:
    i = userfile.read(1)
    if i in numeric:
        continue
    elif i in symbols:
        continue
    elif i == "<":
        while i != ">":
            i = userfile.read(1)
        continue
    elif i == "[":
        while i != "]":
            i = userfile.read(1)
        continue
    elif i == "\n":
        new.write("\n")
    elif i == "":
        break
    else:
        new.write(i)
userfile.close()
print("Conversion Successful.")