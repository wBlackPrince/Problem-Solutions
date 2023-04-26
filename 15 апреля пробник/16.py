def f(n):
   if n == 0: return 9
   if n>0 and n%9 == 0: return n/3 + f(n/3)
   return n/2 + f(n/2)

mas = []
for i in range(0,1000001):
   if 1 <= f(i) <= 1_000_000:
      mas.append(i)
print(len(set(mas)))