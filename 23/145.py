def f(start,count=0):
   if count > 15: return 0
   if count == 15: return [start]

   return f(start * 2, count + 1) +  f(start*2 + 1, count + 1)  

print(len(set(f(1))))
# 32768