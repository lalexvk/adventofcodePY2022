
with open("input.in") as file:
    rounds = [i for i in file.read().strip().split("\n")]

results = {
"A X":4, "A Y":8,"A Z":3,
"B X":1, "B Y":5,"B Z":9,
"C X":7, "C Y":2,"C Z":6
}

resultsP2 = {
"A X":3, "A Y":4,"A Z":8,
"B X":1, "B Y":5,"B Z":9,
"C X":2, "C Y":6,"C Z":7
}

total_points = 0
for round in rounds:
    total_points +=  results[round]

total_points_p2 = 0
for round in rounds:
    total_points_p2 +=  resultsP2[round]

print("Respuesta1:" + str(total_points))
print("Respuesta2:" + str(total_points_p2))