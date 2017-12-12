with open(r"C:\kr.txt", encoding = "utf-8") as f:
 lines = f.readlines()
 for line in lines:
    words = line.split("|")
    for i in range (len(words[0])):
             if i >= 20:   
              print(line)
