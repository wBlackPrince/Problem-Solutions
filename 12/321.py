def f(s):
   while ">2<" not in s:
      s0 = s
      s = s.replace('>1', '>2', 1)
      s = s.replace('12<', '1<2', 1 )
      s = s.replace('>21', '1>', 1)
      s = s.replace('1<', '<2', 1)
      if s0 == s: return False
   return s

s = ">2" + "12"*42 +"<"
summi = sum([int(i) for i in f(s) if i.isdigit()])
print(summi)

#42
