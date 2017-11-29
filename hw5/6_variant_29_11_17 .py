nums=[] 
num=0
for num in range(7): 
  num = int(input("Введите число: "))
  nums.append(num)
with open("homework.txt", "w", encoding="utf-8") as f:
 for n in nums:
  if n < 0:
    lines = ""
  else:
    lines = "X" * n
  print(lines)
  f.writelines(lines +"\n")

