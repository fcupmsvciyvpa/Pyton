a = 10
b = -5
my_dir = {}
for i in range(a, b-1, -1):
   my_dir[i] = i ** i
   print(f"{i}: {my_dir[i]}")