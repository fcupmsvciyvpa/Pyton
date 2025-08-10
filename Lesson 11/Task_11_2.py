pets = {

   1:

        {

            "Мухтар": {

                "Вид питомца": "Собака",

                "Возраст питомца": 9,

                "Имя владельца": "Павел"

            },

        },
   2:
        {

            "Каа": {

                "Вид питомца": "желторотый питон",

                "Возраст питомца": 19,

                "Имя владельца": "Саша"

            }

        }
}
character = {}
command = ""

# Функции для поиска пустых ID
def get_next_id():
   tmp_number = max(pets.keys()) +1 if pets else 1
   if tmp_number == 1:
      return 1
   for p in range(1,tmp_number+1):
      if p not in pets.keys():
         return p
    
# для вывода информации о питомце по ID
# если ID не найден, то возвращает False
def get_pet(ID):
   return pets[ID] if ID in pets.keys() else False

# Функция для получения суффикса возраста
def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"

# Функция для получения списка питомцев
def get_list():
   for i in sorted(pets):
      print(f"ID: {i}, Имя питомца:" ,*pets[i].keys())

# добавление новых питомцев
def create():
   new_id = get_next_id()
   pet_name = input("Введите имя питомца: ")
   character = {
      'Вид питомца': input("Введите вид питомца: "),
      'Возраст питомца': int(input("Введите возраст питомца: ")),  
      'Имя владельца': input("Введите имя владельца: ")
      }
   pets[new_id] = {pet_name: character}



# Чтение питомцев
def read():
   get_list() if input("Вывести список питомцев? \n\r(Ввидите Y для получения краткой информации, или нажмите Enter чтобы продолжить): ").lower() == 'y' else None

   tmp_id = int(input("Ввидите id питомца для просмотра информации: "))
   if tmp_id in pets.keys():
      tmp_pets_item = get_pet(tmp_id)
      for tmp_pet_item,tmp_pet_item1 in tmp_pets_item.items():
         tmp_pet_name = tmp_pet_item
         pet_type = tmp_pet_item1['Вид питомца']
         pet_age = tmp_pet_item1['Возраст питомца']
         owner_name = tmp_pet_item1['Имя владельца']
         age_suffix = get_suffix(pet_age)
         print(f'Это {pet_type} по кличке "{tmp_pet_name}". Возраст питомца: {pet_age} {age_suffix}. Имя владельца: {owner_name}')   
   else:
      print("Питомец с таким ID не найден.")

# Функции для обновления информации о питомце
def update():
   get_list() if input("Вывести список питомцев? (Ввидите Y для продолжения): ").lower() == 'y' else None

   tmp_id = int(input("Ввидите id питомца для изменения информации: "))
   if tmp_id in pets.keys():
      pet_name = input("Введите имя питомца (или напишите exit для завершения): ")
      
      character = {
         'Вид питомца': input("Введите вид питомца: "),
         'Возраст питомца': int(input("Введите возраст питомца: ")),  
         'Имя владельца': input("Введите имя владельца: ")
         }
      pets[tmp_id] = {pet_name: character}
   else:
      print("Питомец с таким ID не найден.")

# Функция для удаления питомца
def delete():
   get_list() if input("Вывести список питомцев? \n\r(Ввидите Y для получения краткой информации, или нажмите Enter чтобы продолжить): ").lower() == 'y' else None   
   tmp_id = int(input("Ввидите id питомца для удаления: "))
   if tmp_id in pets.keys():
      del pets[tmp_id]
      print(f"Питомец с ID {tmp_id} был удален.")

# Основной цикл программы
while command != "stop":
      command = input("Введите команду (Напишите stop или нажмите ENTER для завершения: ").lower()
      if command == "create":
          create()
      elif command == "read":
          read()
      elif command == "update":
          update()
      elif command == "delete":
          delete()
      elif command == "stop" or command == "":
          print("Завершение программы.")
          break
      else:
          print("Неизвестная команда. Пожалуйста, попробуйте снова.")
