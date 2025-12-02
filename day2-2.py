import re #import regular expression :D

def getfactors(x):
    factors = []
    for i in range(1, x + 1):
       if x % i == 0:
           factors.append(i)
    return factors

rangelist = input("h:").split(",")
# max length of invalid is 6, and all invalid ids have an even length
for x in range(0, len(rangelist)): #turns list into a 2d list
    rangelist[x] = rangelist[x].split("-")
rangelist = [[int(y[0]), int(y[1])] for y in rangelist] #turns all ranges upper and lower bounds into ints
print(rangelist)
rangematch = []
for idrange in rangelist: 
    for i in range(idrange[0], idrange[1]):
        # print(x) # it was too much lol
        lenfactor = getfactors(len(str(i)))
        for ii in range(1, len(str(i))): #might add +1
            for factor2 in lenfactor:
                match = re.search(rf"(.{{{factor2}}})\1{{{ii}}}", str(i)) 
                if match:
                    rangematch.append(int(match.group())) #add the match to a group
print("------")
print(rangematch)
print(sum(rangematch))
