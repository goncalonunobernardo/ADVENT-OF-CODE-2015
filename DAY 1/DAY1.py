#PART 1 OF DAY 1 - ADVENT OF CODE 2015

strfile = open("DAY1.txt").read()
#The default mode for open is read-only, so you don’t need to specify the ‘r’ flag.
floor = 0

for i in range(0, len(strfile)):
 if strfile[i] == '(':
    floor += 1
 elif strfile[i] == ')':
    floor -= 1
    if floor == -1: #PART 2 STARTS HERE
        print("SANTA CLAUS ENTERED BASEMENT IN POSITION NUMBER")
        print(i + 1)
        print("\n")


print("The floor Santa Claus needs to know is")
print(int(floor))
