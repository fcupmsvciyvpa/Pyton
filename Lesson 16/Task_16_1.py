# Задание №1

# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:

# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег


class cassa(object):
    def __init__(self, b=0):
        self.balance = b

    def top_up(self, X):
        self.balance += X
        print(f"Баланс пополнен на {X}. Текущий баланс: {self.balance}")

    def get_suffix(self, age):
        if age % 10 == 1 and age % 100 != 11:
            return "целая тысяча"
        elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
            return "целые тысячи"
        else:
            return "целых тысяч"

    def count_1000(self):
        i = 0
        cmt = self.balance 
        while cmt >= 1000:
            cmt -= 1000
            i += 1
        print(f"В кассе есть {i} {self.get_suffix(i)}. Текущий баланс: {self.balance}")
        

    def take_away(self, X): 
        if self.balance >= X:
            self.balance -= X
            print(f"Снято {X}. Текущий баланс: {self.balance}")
        else:
            print(f"Недостаточно средств для снятия {X}.")

command = ""

my = cassa()



while command != "stop":
      command = input("Введите команду (Напишите stop или нажмите ENTER для завершения: ").lower()
      if command == "top_up":
          my.top_up(int(input("Введите сумму для пополнения: ")))
      elif command == "count_1000":
          my.count_1000()
      elif command == "take_away":
          my.take_away(int(input("Введите сумму для снятия: ")))
      elif command == "stop" or command == "":
          print("Завершение программы.")
          break
      else:
          print("Неизвестная команда. Пожалуйста, попробуйте снова.")
