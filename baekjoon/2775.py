num = int(input())

for _ in range(num):
    k = int(input())
    n = int(input())
    f = [x for x in range(1,n+1)]
    for _ in range(k):
        for j in range(1, n):
            f[j] += f[j-1]
    print(f[-1])