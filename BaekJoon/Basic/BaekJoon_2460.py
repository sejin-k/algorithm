station = []
current = 0
max_people = 0
for i in range(10): station.append(list(map(int, input().split())))

for state in station:
    current -= state[0]
    current += state[1]
    if current > max_people: max_people = current

print(max_people)