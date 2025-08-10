my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ]

def recursiv(n=0):
    if n > my_list[-1]:
         print(f"Конец списка")
         return
    print(my_list[n])
    recursiv(n + 1)
    
    return my_list[n]

recursiv()