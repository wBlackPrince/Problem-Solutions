def f(start, end, s = ""):
   if start > end: return 0
   if end == start and "BBA" not in s: return 1
   
   return f(start+2, end, s+"B") + f(start*2, end, s+"A")

print(f(4,42))
#ответ: 10