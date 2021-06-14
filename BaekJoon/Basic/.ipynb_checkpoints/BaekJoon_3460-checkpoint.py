n = int(input())
t_case = []
for i in range(n):
    t_case.append(int(input()))
    
for c in t_case:
    idx = []
    binary = format(c, 'b')
    for i, num in enumerate(binary[::-1]):
        if int(num) == 1:
            idx.append(str(i))
    print(" ".join(idx), end="\n")