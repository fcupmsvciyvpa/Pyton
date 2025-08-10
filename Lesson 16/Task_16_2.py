# Задание №2

# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход

# у этого класс есть методы:

# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

from collections import deque


class turtle(object):

    def __init__(self, x, y, s):

        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        print(f"Текущие координаты черепашки: ({self.x}, {self.y}), скорость: {self.s}")
    def go_down(self):
        self.y -= self.s
        print(f"Текущие координаты черепашки: ({self.x}, {self.y}), скорость: {self.s}")    
    def go_left(self):
        self.x -= self.s
        print(f"Текущие координаты черепашки: ({self.x}, {self.y}), скорость: {self.s}")    
    def go_right(self):
        self.x += self.s
        print(f"Текущие координаты черепашки: ({self.x}, {self.y}), скорость: {self.s}")    
    def evolve(self):
        self.s += 1
        print(f"Текущие координаты черепашки: ({self.x}, {self.y}), скорость: {self.s}")    
    def degrade(self):
        self.s -= 1
        print(f"Текущие координаты черепашки: ({self.x}, {self.y}), скорость: {self.s}")    



    def count_moves(self, x2, y2):
        start_position = (self.x, self.y, self.s)
        queue = deque([(start_position, [], 0)])  # Кортеж: (позиция, путь, шаги)
        visited = set()

        while queue:
            (current_x, current_y, current_s), path, steps = queue.popleft()
            
            # Если достигли целевых координат
            if current_x == x2 and current_y == y2:
                return len(path), path
            
            # Возможные движения (вверх/вниз/влево/вправо)
            possible_moves = [
                ('up', current_x, current_y + current_s, current_s),
                ('down', current_x, current_y - current_s, current_s),
                ('left', current_x - current_s, current_y, current_s),
                ('right', current_x + current_s, current_y, current_s)
            ]
            
            # Возможность изменения шага
            possible_changes = [
                ('evolve', current_x, current_y, current_s + 1),
                ('degrade', current_x, current_y, current_s - 1) if current_s > 1 else None
            ]
            
            # Преобразовываем None в пустоту
            possible_changes = list(filter(None, possible_changes))
            
            # Объединяем движения и изменения шага
            possible_states = possible_moves + possible_changes
            
            # Просматриваем каждое возможное состояние
            for action, new_x, new_y, new_s in possible_states:
                new_state = (new_x, new_y, new_s)
                
                # Проверяем, не было ли такого состояния ранее
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [action], steps + 1))



The_turtle = turtle(-1, 2, 2)

command = ""

while command != "stop":
        command = input("Введите команду для 🐢 (Напишите stop или нажмите ENTER для завершения: ").lower()
        if command == "go_up":
            The_turtle.go_up()
        elif command == "go_down":
            The_turtle.go_down()
        elif command == "go_left":
            The_turtle.go_left()
        elif command == "go_right":
            The_turtle.go_right() 
        elif command == "evolve":
            The_turtle.evolve()
        elif command == "degrade":
            The_turtle.degrade()
        elif command == "count_moves":
            X = int(input("Введите координату X: "))
            Y = int(input("Введите координату Y: "))
            steps_count, moves_sequence = The_turtle.count_moves(X, Y)
            
            print(f"Мин. кол-во шагов: {steps_count}")
            print("Последовательность действий:")
            for i, move in enumerate(moves_sequence):
                print(f"{i+1}. {move.capitalize()}")  

        elif command == "stop" or command == "":
            print("Завершение программы.")
            break
        else:
            print("Неизвестная команда. Пожалуйста, попробуйте снова.")

