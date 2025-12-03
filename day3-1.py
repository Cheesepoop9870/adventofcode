batteries = input("h:").split()
print(batteries)
power = []

for battery in batteries:
    powerlist = []
    for x in range(0, len(battery)):
        for y in range(x, len(battery)):
            if x != y:
                powerlist.append(int(battery[x]+battery[y]))
    print(int(battery[x]+battery[y]))        
    powerlist.sort(reverse=True)
    power.append(powerlist[0])
print("-------")
print(power)
print(sum(power))
    
    
