import re #import regular expression :D
rangelist = input("h:").split(",")
# max length of invalid is 6, and all invalid ids have an even length
for x in range(0, len(rangelist)): #turns list into a 2d list
    rangelist[x] = rangelist[x].split("-")
rangelist = [[int(y[0]), int(y[1])] for y in rangelist] #turns all ranges upper and lower bounds into ints
print(rangelist)
rangematch = []
for idrange in rangelist: 
    for x in range(idrange[0], idrange[1]):
        # print(x)
        if len(str(x)) % 2 == 0: #check if the length is an even amount so it dosent take forever
                match = re.search(rf"(.{{{len(str(x)) // 2 }}})\1", str(x)) #regex to match repeated strings that is half the length of of the actual string
                if match:
                    rangematch.append(int(match.group())) #add the match to a group
print("------")
print(rangematch)
print(sum(rangematch))
