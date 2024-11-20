# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()

# A
# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()

# B
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

# C
# number_of_stars = int(input("Number of stars: "))
# print('*' * number_of_stars)

# D
# number_of_stars = int(input("Number of stars: "))
# for i in range(1, number_of_stars + 1):
#     print('*' * i)
result = 0
for j in range(0, len(numbers)):
    if numbers[j] < 0:
        result = result + 1