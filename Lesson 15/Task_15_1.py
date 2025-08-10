 

class Transport(object):

   def __init__(self, name, max_speed, mileage):

    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage
 
    
def defolt_transport(self):
    Autobus = Transport(name="Renaul Logan", max_speed=180, mileage=12)
    return Autobus

Autobus = Transport(input("Введите название транспорта или нажмите ENTER для установки стандартных параметров: "), 0, 0)
if not Autobus.name:
    Autobus = defolt_transport(Autobus)
else:
    Autobus.max_speed = int(input("Введите максимальную скорость: "))
    Autobus.mileage = int(input("Введите пробег: "))
print(f"Название автомобиля: {Autobus.name} Скорость: {Autobus.max_speed} Пробег: {Autobus.mileage}")