h, m = list(map(int, input().split()))

if m >= 45:
    print(str(h)+' '+str(m-45))
else:
    if h > 0:
        print(str(h-1)+' '+str(m+15))
    else:
        print(str(23)+' '+str(m+15))