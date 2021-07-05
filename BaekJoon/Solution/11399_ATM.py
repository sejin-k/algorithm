n = int(input())
p = list(map(int, input().split()))

p.sort()
result = 0
for i in range(len(p)):
    result += p[i] * (len(p) - i)
    
print(result)