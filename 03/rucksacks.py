pointsPriority = 0

priorities = {
"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,
"A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52
}

with open("input.in") as file:
    data = [i for i in file.read().strip().split("\n")]


for rucksacks in data:
    half = len(rucksacks)//2

    left = set(rucksacks[:half])
    right = set(rucksacks[half:])

    for character in priorities:
        if character in right and character in left:
            pointsPriority += priorities[character]

print("Respuesta 1: ",pointsPriority)

pointsPriority = 0
j = 3

for i in range(0,len(data), 3):
    rucksacks = data[i:j]
    j += 3

    for character in priorities:
            if character in rucksacks[0] and character in rucksacks[1] and character in rucksacks[2]:
                pointsPriority += priorities[character]

print("Respuesta 2: " ,pointsPriority)