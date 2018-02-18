import random

def open_file(fname):
  with open (fname, 'r', encoding='utf-8') as f:
    lines = f.readlines()
  return lines

def dic_words(lines):
  play = input('Хотите сыграть в игру? Введите "да" или "нет": ')
  if play.lower() == 'нет':
    print('Ехх, жаль((')
  elif play.lower() == 'да':
   print('\nПопробуйте с трех попыток угадать слово в словосочетании:') 
   dic = {}
   for line in lines:
      cells = line.split(';')
      word = cells[1][:-1]
      clue = cells[0]
      dic[word] = clue
   key = random.choice(list(dic.keys()))
   print(dic[key], '...')
   answer = input('Какое слово стоит вместо точек? ')
   n = 2
   while n !=0:
    if answer.lower() == key:
        n = 0
    else:
      print('Попробуйте ещё! Количество оставшихся попыток:', n)
      n -=1
      answer = input('\nКакое слово стоит вместо точек? ')
   if n == 0 and answer.lower() == key:
     print('Бинго!')
   else:
     print('Попыток больше нет. Но не расстраивайтесь и возвращайтесь снова!')          
         
def main():
    dic = dic_words(open_file('collocation11.csv'))

if __name__ == '__main__':
    main()
    
