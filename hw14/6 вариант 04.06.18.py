import re

#открываем файл, удаляем пунктуацию и делим на предложения
def open_file(fname):
    with open(fname, encoding = 'utf-8') as f:
        text = f.read()
        text = re.sub('[,:;—"]', '', text)
        nopunct = text.replace('?', '.').replace('!', '.').split('.')      
    return nopunct

#оставляем предложения, в которых больше десяти слов
def find_sent(nopunct):
    new_list = [i for i in nopunct if len(i.split()) > 10]
    return new_list

#считаем среднюю длину слов в предложении
def ave_len(new_list):
    for sentence in new_list:
        len_counter = [len(word) for word in sentence.split()]
        average = sum(len_counter) / len(len_counter)
        print(sentence, '\n^Это предложение со словами длины {}'.format(round(average, 1)), '\n')
    
def main():
    fname = input('Введите имя файла: ')
    nopunct = open_file(fname)
    new_list = find_sent(nopunct)
    ave_len(new_list)

if __name__ == '__main__':
    main()
