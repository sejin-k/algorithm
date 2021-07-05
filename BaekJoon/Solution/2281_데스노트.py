# n(이름의 개수), m(노트 가로줄 개수) 입력
n, m = map(int, input().split())
name_list = [int(input()) for i in range(n)]

# name_list의 i번째 이름부터 시작하는 경우의 최솟값이 든 DP
start = len(name_list)

for i in range(len(name_list) - 1,  -1, -1):
    start = i
    if sum(name_list[i:]) + (len(name_list[i:]) - 1) > m:
        break

DP = [0] * (len(name_list))
case = []

for i in range(start,  -1, -1):
    j = 1
    while True:
        words_len = sum(name_list[i:i+j]) + (len(name_list[i:i+j]) - 1)
#         print(words_len)
        case.append((m - words_len)**2 + DP[i+j])
        j += 1
        if sum(name_list[i:i+j]) + (len(name_list[i:i+j]) - 1) <= m: continue
        break
    DP[i] = min(case)
    words_len = 0
    case = []
        
print(DP[0])