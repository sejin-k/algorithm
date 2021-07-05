dwarfs = []
for i in range(9): dwarfs.append(int(input()))

total = sum(dwarfs)
gap = total - 100
for i in range(len(dwarfs)):
    for j in range(i+1, len(dwarfs)):
        if dwarfs[i] + dwarfs[j] == gap:
            del dwarfs[j], dwarfs[i]
            dwarfs.sort()
            break
            
print("\n".join(map(str, dwarfs)))