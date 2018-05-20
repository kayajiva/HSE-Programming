import os
from collections import Counter

#собираем пути и приводим их к виду 'папка?расширение'
#символ '?' нужен для того, чтобы потом отделить имя папки от расширения

def collect_paths():
    dir_ext = []
    start_path = '.'
    for root, dirs, files in os.walk(start_path):
     for file in files:
       filepath = os.path.join(root, file)
       dr = os.path.split(filepath)[0][2::]
       ext = os.path.splitext(filepath)[1]
       dic = dr + '?' + ext
       dir_ext.append(dic)
    return dir_ext

#делаем словарь частотности вхождений типа 'папка?расширение'
#оставляем только те, которые встречаются больше 1 раза

def freq_dic(dir_ext):
    dic = {}
    freq = dict(Counter(dir_ext))
    for k, v in freq.items():
        if v != 1:
            dic.update({k: v})
    return dic

#отделяем имена папок от расширений
#считаем, в скольких папках есть файлы с одним расширением

def count_dirs(dic):
    spis2 = []
    for k in dic.keys():
        if k.split('?')[0] not in spis2:
         spis2.append(k.split('?')[0])
    print('Папок, в которых встречаются файлы с одинаковыми расширениями: ', len(spis2))


def main():
    dir_ext = collect_paths()
    dic = freq_dic(dir_ext)
    count_dirs(dic)

    
if __name__ == '__main__':
    main()
