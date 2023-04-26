with open("17.txt") as f:
   a = [int(i) for i in f.readlines()]

summi = sum([i for i in a if i%16 == 0])

def checker(a,b):
   cond_1 = all([hex(a)[-1] == "f", hex(b)[-1] == "f"])
   cond_2 = any([summi >= 0 and a+b >= 0, summi <= 0 and a+b <= 0])
   return cond_1 and cond_2

mas = []
for i in range(len(a)-1):
   if checker(a[i],a[i+1]):
      mas.append(a[i] + a[i+1])

print(len(mas), max(mas))