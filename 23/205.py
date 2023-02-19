def f(start, end, s=""):
   if start == end and s.count("1") <= 4 and s.count("2") >= 2 and s.count("3") == 5: return 1
   if start > end: return 0
   
   return f(start*5, end, s + "1") + f(start*3, end, s + "2") + f(start + 45, end, s + "3")

print(f(1,2970))
# 74