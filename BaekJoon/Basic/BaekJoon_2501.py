# 1. 약수 전체를 구하는 방법
import math
n, k = map(int, input().split())

divisor = []
count = 0
for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
        divisor.extend([i, n//i])
        
divisor = list(set(divisor))
divisor.sort()

if len(divisor) < k: print(0)
else: print(divisor[k-1])

#####################################
# # 문제에만 만족하는 풀이
# import math
# n, k = map(int, input().split())

# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
#         if count == k:
#             result = i
#             break
# else:
#     result = 0
# print(result)