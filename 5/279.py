def f(n):
   s = str(n)
   not_evaul_nums = sum([int(i) for i in s if int(i)%2 != 0])
   evaul_pos = sum([int(s[i]) for i in range(len(s)) if i%2 != 0])
   return abs(not_evaul_nums - evaul_pos)

for i in range(10_000_000,20_000_000):
   if f(i) == 29:
      print(i)
      break
#16080808