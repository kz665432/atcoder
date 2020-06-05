num_500_yen = int(input())  # 500 yen
num_100_yen = int(input())  # 100 yen
num_50_yen = int(input())  # 50 yen
x = int(input())  # sum

count = 0
for i in range(num_500_yen+1):
    for j in range(num_100_yen+1):
        for k in range(num_50_yen+1):
            sum = 500 * i + 100 * j + 50 * k
            if sum == x:
                count += 1

print(count)
