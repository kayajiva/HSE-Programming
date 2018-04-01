#можно чекать по файлам wombat или poloskun

import re

def open_page(fname):
    with open (fname + '.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

#отряд животного на странице - это первая фраза кириллицей
#которая встречается после слова "Отряд" внутри тегов    
def find_order(text):
    order = re.findall('Отряд.+?>([А-я].+?)<', text)[0]
    return order

def write_order(order):
    with open ('order.txt', 'w', encoding = 'utf-8') as f:
        order_file = f.write(order)
    return order_file 
    
def main():
    fname = input('Введите имя интернет-страницы без расширения: ')
    text = open_page(fname)
    order = find_order(text)
    order_file = write_order(order)
    print('\nПроспойлерим отряд перед тем, как Вы откроете файл:')
    print(order)

if __name__ == '__main__':
    main()

