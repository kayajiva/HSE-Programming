import os
import re

#ищем файлы и папки
def find_items():
    items = os.listdir()
    return items 

#оставляем только файлы
def find_files(items):
    files = []
    for item in items:
        if '.' in item:
            files.append(item)
    return files

#ищем файлы со знаками препинания в названии
def find_punct(files):
    str_files = (' ').join(files)
    fnames = re.findall('([\s\S].+?)\.[a-z].+? ', str_files)
    print(fnames)
    punct = '.,:;!?—"'
    punct_counter = 0
    for i in punct:
        for fname in fnames:
            if i in fname:
                punct_counter +=1
    return punct_counter

def main():
    items = find_items()
    files = find_files(items)
    punct_counter = find_punct(files)
    print('Всего файлов со знаками препинания в названии: ', punct_counter)

if __name__ == '__main__':
    main()
    

