N= int(input("Введите количество чисел: "))
cnt = 0
for i in range(N):
    number = int(input("Введите целое число: "))
    if number == 0:
        cnt += 1
print("Количество чисел равные нулю:",cnt)