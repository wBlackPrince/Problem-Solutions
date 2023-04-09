def checker(n):
   for i in range(2,n//2+1):
      if  n%i == 0: return False
   return True


for n in range(2,100):
   g = 9 + 3*n + 5*n
   if checker(g) and 1000 > g >= 100:
      print(n)
      break