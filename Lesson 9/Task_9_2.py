n = list(map(float, input().split()))
v = list(map(float, input().split()))

if len(n) <= 10 ** 4 and len(v) <= 10 ** 4:
    print(len(set(n).intersection(set(v))))
else:
    print("Введены некоректные числа")