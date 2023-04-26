from itertools import product

a = ["".join(i) for i in product("АЕИЛНПСЬ",repeat = 4)]

for i in range(len(a)):
   if a[i][:2] == "ПЕ":
      print(i+1)
      break