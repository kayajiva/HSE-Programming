#в Pride and Prejudice нет слов с omni-
#поэтому удобнее проверять по файлу 'check'

#чтобы найти слова на omni- по регулярным выражениям, импортируем модуль re:
import re 

#открываем файл:
def open_file(fname): 
   with open (fname + '.txt', 'r', encoding = 'utf-8') as f: 
     text = f.read()
     text = text.lower()
   return text

#ищем слова на omni-, установив границу по правому контексту:
def find_omni(text):
    omnilist = re.findall('(omni.+?)[ .,:;"!?)]', text)
    return omnilist

#считаем частотность для слов на omni-:
def freq_omni(fname):
    words = open_file(fname).split()
    omnilist = find_omni(open_file(fname))
    freq_omni = len(omnilist) / len(words)
    return freq_omni

#ищем слова без omni-:
def find_none(fname):
   nonelist = []
   words = open_file(fname).split()
   omnilist = find_omni(open_file(fname))
   for word in omnilist:
      if word[4:] in words:
         nonelist.append(word)
   return nonelist 

#считаем для них частотность:
def freq_none(fname):
   words = open_file(fname).split()
   nonelist = find_none(fname)
   freq_none = len(nonelist) / len(words)
   return freq_none

#спрашиваем имя файла и выводим результаты:   
def main():
   a = input('Введите имя файла без расширения: ')
   print('Частотность с omni: ', freq_omni(a))
   print('Частотность без omni: ', freq_none(a))
   
main()
