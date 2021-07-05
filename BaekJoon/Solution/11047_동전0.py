num, total = list(map(int, input().split()))
coins = []
for i in range(num):
    coins.append(int(input()))
coins.sort(reverse=True)

result = 0
for coin in coins:
    if total >= coin:
        a, b = divmod(total, coin)
        result += a
        if b == 0:
            break
        else:
            total = b
            
print(result)