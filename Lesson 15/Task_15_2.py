class Transport(object):
    name = "Renaul Logan"
    max_speed = 180
    mileage = 12
    capacity = 50
    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    

    def seating_capacity(self, capacity):

       return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


cmt = input("Введите название транспорта или нажмите ENTER для установки стандартных параметров: ")
capacity = input("Введите вместимость одного автобуса или нажмите ENTER для установки стандартных параметров: ")
if not cmt:
    Autobus = Transport("Renaul Logan", 180, 12)
else:
    Autobus = Transport(cmt, 180, 12)
if not capacity:
    print(Autobus.seating_capacity(capacity = 50 ))
else:    
    print(Autobus.seating_capacity(capacity=int(capacity)))
