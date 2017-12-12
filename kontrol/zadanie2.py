sum = 0
with open(r"C:\kr.txt", encoding = "utf-8") as f:
 lines = f.readlines()
 for line in lines:
    words = line.split("|")
    for word in words[2]:
     if word != "":
         sum += 1
print(sum)
