elves = []

temp = 0
#read file
with open('calories.in', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            #when is a empty line save the sum to the array and reset sum
            elves.append(temp)
            temp = 0
            continue
        x = int(line)
        temp += x
#sort from greather to smaller
elves.sort(reverse=True)
#get the max
print("Respuesta 1: ",max(elves))
#get the 3 greather
print("Respuesta 2: ",sum(elves[:3]))