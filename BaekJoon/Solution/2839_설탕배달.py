total = int(input())

max_5 = total // 5

for i in range(max_5,-1,-1):
    check = (total - (5 * i)) % 3
    if check == 0:
        result = i + ((total - (5 * i)) // 3)
        break
else:
    if check != 0:
        result = -1

print(result)