# 두 문자열 입력
str_A = input()
str_B = input()

LCS = [[0]*(len(str_B) + 1) for i in range(len(str_A) + 1)]

for i in range(len(str_A) + 1):
    for j in range(len(str_B) + 1):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif str_A[i - 1] == str_B[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[-1][-1])