import re

def open_page(pname):
    with open(pname + '.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def word_sub(text):
    word1 = re.sub('Финляндия', 'Малайзия', text)
    word2 = re.sub('Финляндии', 'Малайзии', text)
    word3 = re.sub('Финляндию', 'Малайзию', text)
    word4 = re.sub('Финляндией', 'Малайзией', text)
    word5 = re.sub('Финляндиею', 'Малайзиею', text)
    text2 = word1 + word2 + word3 + word4 + word5
    return text2

def write_text(text2):
    with open('text_sub.txt', 'w', encoding = 'utf-8') as f:
        text_sub = f.write(text2)
    return text_sub

def main():
    pname = input('Введите имя страницы: ')
    text = open_page(pname)
    text2 = word_sub(text)
    text_sub = write_text(text2)

if __name__ == '__main__':
    main()
