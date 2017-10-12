#PART 1 OF DAY 2 - ADVENT OF CODE 2015

quantitypaper = 0
#Initializing total paper needed

strfile = open("DAY2.txt").read()
#The default mode for open is read-only, so you don’t need to specify the ‘r’ flag
strfile = strfile.split()
#Getting rid of the new lines first gives me a list of every line

for line in strfile:
    #Get length, width and height by splitting the string whenever he checks 'x'
    l, w, h = line.split('x')
    l, w, h = int(l), int(w), int(h)
    #Calculating the area of each side
    al, aw, ah = l*w, w*h, h*l
    #Adding the smallest area
    extra = min(al,aw,ah)
    #Adding the full area
    quantitypaper += 2* (al +aw + ah) + extra

print(quantitypaper)
#FINISHED PART1 // PART 2 BEGINS NOW