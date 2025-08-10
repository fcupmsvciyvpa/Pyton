import random

def print_matrix(matrix):
    for i in matrix:
        print(i,)
    print("\n\r\n\r")

a = [[random.randint(-10000, 10000) for i in range(10)] for j in range(10)]
b = [[random.randint(-10000, 10000) for i in range(10)] for j in range(10)]
sum_a_b = [[0 for i in range(10)] for j in range(10)]


for i in range(len(sum_a_b)):
    for j in range(len(sum_a_b[i])):
        sum_a_b[i][j] = a[i][j] + b[i][j]

print_matrix(a)
print_matrix(b)
print_matrix(sum_a_b)