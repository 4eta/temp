a = input()
b = input()
c = [""] * (len(b) + 1)

for i in range(1, len(a) + 1):
    cprev = c.copy()
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            c[j] = cprev[j-1] + a[i-1]
        else:
            c[j] = max(c[j-1], cprev[j], key=len)

print(c[-1])
