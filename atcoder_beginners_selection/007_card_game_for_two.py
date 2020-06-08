n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

alice = 0
bob = 0
for t, i in enumerate(a):
    if t % 2 == 0:
        alice += i
    else:
        bob += i

print(alice - bob)
