import collections
import re

def open_file():
    with open ('F.xml', 'r', encoding = 'utf-8') as f:
        lines = f.read()
    return lines

def make_dic(lines):
    dictum = {}
    gr_values = re.findall('w lemma=.+?type="(.+?)">', lines)
    strvalue = ' '.join(gr_values)
    newdict = dictum.update(strvalue)
    counting = Counter(newdict)
    return counting

def write_file(counting):
    with open('dicti.txt', 'w', encoding = 'utf-8') as r:
        dicti = r.write(counting)
    return dicti
    
def main():
    lines = open_file()
    counting = make_dic(lines)
    dicti = write_file(counting)
    print(counting)

if __name__ == '__main__':
    main()
