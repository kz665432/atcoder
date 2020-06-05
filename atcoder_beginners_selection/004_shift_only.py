n = int(input())
a = list(map(int, input().split()))
iter = -1
while True:
    iter += 1
    for i in range(n):
        if a[i] % 2 == 1:
            break
        else:
            a[i] /= 2
    else:
        continue
    break
print(iter)
