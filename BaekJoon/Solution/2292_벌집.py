d = int(input())

n=1
max_num = 1
while True:
    max_num += (n-1)*6
    if max_num >= d:
        break
    else:
        n += 1
        

print(n)