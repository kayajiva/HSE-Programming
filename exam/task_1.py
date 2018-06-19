import re
import os

def read_data():
    namelist = []
    path = '.'
    for file_names in os.listdir(path):
        with open (os.path.join(path, file_names), encoding = 'windows-1251') as f:
            data = f.read()
            title = re.findall('<title>([\s\S].+?)</title>', data)
            tagging = re.findall('<meta content="([\s\S].+?)" name="tagging"', data)
            author = re.findall('<meta content="([\s\S].+?)" name="author"', data)
            created = re.findall('<meta content="([\s\S].+?)" name="created"', data)
            topic = re.findall('<meta content="([\s\S].+?)" name="topic"', data)
            doc_id = re.findall('<meta content="([\s\S].+?)" name="docid"', data)
            namelist.append(title)
            namelist.append(tagging)
            namelist.append(author)
            namelist.append(created)
            namelist.append(doc_id)
            namelist.append(topic)
    print(namelist)
    return namelist


def write_text(namelist):
    with open('name_file.csv', 'w', encoding = 'windows-1251') as f:
        text_new = f.write(str(namelist))
    return text_new
   
                    
                
    
def main():
    namelist = read_data()
    write_text(namelist)
    
if __name__ == '__main__':
    main()
