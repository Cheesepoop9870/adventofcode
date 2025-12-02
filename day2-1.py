import re #import regular expression :D
rangelist = input("h:").split(",")
# max length of invalid is 6, and all invalid ids have an even length
for x in range(0, len(rangelist)): #turns list into a 2d list
    rangelist[x] = rangelist[x].split("-")
rangelist = [[int(y[0]), int(y[1])] for y in rangelist]
print(rangelist)
