fname = r"C:\Users\User\text.txt"
with open(fname, encoding="utf-8") as f:
    text=f.read()
words = text.split()
cap = 0
low = 0
for word in words:
        if word.istitle():
         cap+=1
        else:
         low+=1
       
percent = cap/(cap+low)*100
print ("Процент слов с заглавной буквы:", int(percent),"%")
