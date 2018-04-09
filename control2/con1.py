import re

def open_file():
    with open('F.xml', encoding = 'utf-8') as f:
        lines = f.read()
    return lines

def counting(lines):
    linestr = re.findall(r'[\s\S](\n)</teiHeader>', lines)
    
    return linestr

def write_file(linestr):
    with open('writedoc.txt', 'w', encoding = 'utf-8') as r:
        writedoc = r.write(str(linestr))
    return writedoc

def main():
    lines = open_file()
    linestr = counting(lines)
    writedoc = write_file(linestr)
    print(linestr)

if __name__ == '__main__':
    main()
