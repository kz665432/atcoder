n, a, b = list(map(int, input().split()))

num_list = []
for num in range(n+1):
    sum_result = 0
    for i in range(len(str(num))):
        sum_result += int(str(num)[i])
    if sum_result >= a and sum_result <= b:
        num_list.append(num)
print(sum(num_list))
