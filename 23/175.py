def f(start, end, s = ""):
   if start in [25,30] or start > end: return 0
   if start == end and "33" not in s: return 1
   
   return f(start + 1, end, s+"1") +  f(start+2, end, s+"2") +  f(start*3, end, s+"3")

print(f(1,15)*f(15,43))
#36253635