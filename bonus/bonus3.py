text = input("Print your text here: ")
for s in [".", ",", "!", "?", ":", "'", '"']:
 text = text.replace(s, "")
words = text.split()
vowels = ["e", "y", "u", "i", "o", "a", "E", "Y", "U", "I", "O", "A"]
ntext=[]
for word in words:
    for letter in word[0]:
        if not letter in vowels:
            nword = word[1:] + word[0].lower() + "ay"
            ntext.append(nword)
        else:
            nword = word[0].lower() + word[1:] + "ay"
            ntext.append(nword)
fin = " ".join(ntext)
print(fin)
