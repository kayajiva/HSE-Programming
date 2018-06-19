import re
import os

def read_data():
    abbr_list = []
    path = r'C:\Users\kayajiva\Desktop\news'
    for file_names in os.listdir(path):
        with open (os.path.join(path, file_names), encoding = 'windows-1251') as f:
            data = f.read()
            abbr = re.findall('([А-Я].+?)', data)
            if len(abbr) >= 2:
                abbr_list.append(abbr)
    print(len(abbr_list))

def main():
    read_data()
    
if __name__ == '__main__':
    main()
