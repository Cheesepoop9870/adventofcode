dial = 50
directions = input("h:").split('\r')
# directions.pop(len(directions)-1)
directions_pm = []
directions_amt = []
direction_result_list = []
direction_pass = 0
direction_pass_list = []
for direction in directions:
    directions_pm.append(direction[0])
    directions_amt.append(int(direction[1:]))
print(directions)
print("")
print(directions_pm)
print(directions_amt)
for x in range(0, len(directions)):
    direction_pass = 0
    if directions_pm[x] == 'L':
        direction_pass = directions_amt[x]//100
        direction_temp = directions_amt[x] % 100
        dial = dial - direction_temp
        if dial < 0:
            dial = dial+100
            direction_pass = direction_pass + 1
        direction_result_list.append(dial)
        direction_pass_list.append(direction_pass)
    elif directions_pm[x] == 'R':
        direction_pass = directions_amt[x]//100
        direction_temp = directions_amt[x] % 100
        dial = dial + direction_temp
        if dial > 99:
            dial = dial-100
            direction_pass += 1 
        direction_result_list.append(dial)
        direction_pass_list.append(direction_pass)
print("----------")
print(direction_result_list)
print("----------")
print(direction_result_list.count(0))
print(direction_result_list.count(0)+direction_pass)
                
