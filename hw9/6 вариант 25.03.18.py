import re

def open_file(fname):
    with open (fname, 'r', encoding = 'utf-8') as f:
        text = f.read()
    text = text.replace('\ufeff', '')
    text = text.lower()
    return text
    
def find_words(text):
#причастия страд.прош. во всех падежных формах
    words1 = re.findall('загруженн?[аоыу]?[а-я]?[а-я]?', text)
#причастия действ.прош. во всех падежных формах
    words2 = re.findall('загрузив?ш?[аеиу]?[а-я]?[а-я]?с?[яь]?', text)
#1 лицо ед. число буд. время
    words3 = re.findall('загружус?[яь]?', text)
#всё остальное
    words4 = re.findall('загруз[ия][мтшл]?[иаоеь]?с?[яь]?', text)
    words = words1 + words2 + words3 + words4
    return words

def write_words(words):
    final = []
    for word in words:
        if not word in final:
           final.append(word)
    return final
        
def main():
    fname = input('Введите имя файла: ')
    text = open_file(fname)
    words = find_words(text)
    final = write_words(words)
    print(final)

if __name__ == '__main__':
    main()
