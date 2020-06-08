n, y = list(map(int, input().split()))

a = b = c = 0

yen_a = 10000
yen_b = 5000
yen_c = 1000

target = y - yen_c * n
coef_a = yen_a - yen_c
coef_b = yen_b - yen_c
a = int(target / coef_a)
if a > n or target < 0:
    a = b = c = -1
else:
    while a >= 0:
        if coef_a * a + coef_b * b == target and n-a-b >= 0:
            c = n - a - b
            break
        elif coef_a * a + coef_b * b > target:
            a -= 1
        else:
            b += 1
    if a == -1:
        b = c = -1

print(a, b, c)


# Algorithm for finding the minimum number
# This is wrong
# a = int(y / 10000)
# if n < a:
#     a = -1
#     b = -1
#     c = -1
# else:
#     y -= 10000 * a
#     b = int(y / 5000)
#     if n < a+b:
#         a = -1
#         b = -1
#         c = -1
#     else:
#         y -= 5000 * b
#         c = int(y / 1000)
#         if n < a+b+c:
#             a = -1
#             b = -1
#             c = -1

# print('{} {} {}'.format(a, b, c))
