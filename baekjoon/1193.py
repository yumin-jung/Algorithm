n = int(input())
l = 1

while n > l:
    n -= l
    l += 1

if l % 2 == 0:
    a = n
    b = l-n+1
else:
    a = l-n+1
    b = n

print(f'{a}/{b}')
