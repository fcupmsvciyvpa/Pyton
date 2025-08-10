
pets = {}
pet_name = " "
while pet_name not in "exit":
    pet_name = input("Введите имя питомца (или напишите exit для завершения): ")
    if pet_name != "exit":
        pets[pet_name] = {
            'Вид питомца': input("Введите вид питомца: "),
            'Возраст питомца': int(input("Введите возраст питомца: ")),  
            'Имя владельца': input("Введите имя владельца: ")
        }


for pet_name, pet_info in pets.items():
    pet_type = pet_info['Вид питомца']
    pet_age = pet_info['Возраст питомца']
    owner_name = pet_info['Имя владельца']
    if pet_age % 10 == 1 and pet_age % 100 != 11:
        age_suffix = "год"
    elif 2 <= pet_age % 10 <= 4 and (pet_age % 100 < 10 or pet_age % 100 >= 20):
        age_suffix = "года"
    else:
        age_suffix = "лет"
    

    info_string = f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_suffix}. Имя владельца: {owner_name}'
    print(info_string)
