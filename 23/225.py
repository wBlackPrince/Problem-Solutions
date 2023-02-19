def f(start, end):
   if start > end: return 0
   if end == start: return 1
   
   return f(start+1, end) + f(start*2, end)

c = sum([f(3,20)*f(20,43), 
   f(3,20)*f(20,47),
   f(7,20)*f(20,43),
   f(7,20)*f(20,47)])

print(c)
# 184