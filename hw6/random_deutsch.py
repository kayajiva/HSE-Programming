import random

#пишем универсальную функцию для открытия файлов:
def open_file(f_name):
    with open(f_name, encoding = 'utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

#открываем с её помощью все необходимые файлы:        
def subjects():
    open_file('E:/random_deutsch/subjects.txt')
    return open_file('E:/random_deutsch/subjects.txt')

def subjectscap():
    open_file('E:/random_deutsch/subjectscap.txt')
    return open_file('E:/random_deutsch/subjectscap.txt')

def objects():
    open_file('E:/random_deutsch/objects.txt') 
    return open_file('E:/random_deutsch/objects.txt')
 
def intrverbs():
    open_file('E:/random_deutsch/intr_verbs.txt') 
    return open_file('E:/random_deutsch/intr_verbs.txt')

def intrverbscap():
    open_file('E:/random_deutsch/intr_verbscap.txt')
    return open_file('E:/random_deutsch/intr_verbscap.txt')

def trverbs():
    open_file('E:/random_deutsch/tr_verbs.txt') 
    return open_file('E:/random_deutsch/tr_verbs.txt')

def trverbscap():
    open_file('E:/random_deutsch/tr_verbscap.txt') 
    return open_file('E:/random_deutsch/tr_verbscap.txt')

def impintr2():
    open_file('E:/random_deutsch/impintr2.txt') 
    return open_file('E:/random_deutsch/impintr2.txt')

def impintr3():
    open_file('E:/random_deutsch/impintr3.txt')
    return open_file('E:/random_deutsch/impintr3.txt')

def imptr2():
    open_file('E:/random_deutsch/imptr2.txt') 
    return open_file('E:/random_deutsch/imptr2.txt')

def imptr3():
    open_file('E:/random_deutsch/imptr3.txt')
    return open_file('E:/random_deutsch/imptr3.txt')

def adverbs():
    open_file('E:/random_deutsch/adverbs.txt')
    return open_file('E:/random_deutsch/adverbs.txt')

#теперь составляем из случайных слов 5 типов предложений
#в каждом типе будет несколько вариантов, которые потом выберутся рандомно

#варианты утвердительных:
def affirmative1():
    return subjectscap() + ' ' + intrverbs() + ' ' + adverbs() + '.'

def affirmative2():
    return subjectscap() + ' ' + trverbs() + ' ' + objects() + ' ' + adverbs() + '.'

#побудительных:
def incentive1():
    return imptr2() + ' ' + 'bitte' + ' ' + objects() + ' ' + adverbs() + '!'

def incentive2():
    return imptr3() + ' ' + 'bitte' + ' ' + objects() + ' ' + adverbs() + '!'

#условных:
def condition1():
    return 'Wenn' + ' ' + subjects() + ' ' + objects() + ' ' + trverbs() + ',' + ' '+ trverbs() +\
           ' ' + subjects() + ' ' + objects() + '.'
def condition2():
    return 'Wenn' + ' ' + subjects() + ' ' + intrverbs() + ','+ ' ' + trverbs() +\
           ' ' + subjects() + ' ' + objects() + '.'
#вопросительных:
def question1():
    return intrverbscap() + ' ' + subjects() + ' ' + adverbs() + '?'

def question2():
    return trverbscap() + ' ' + subjects() + ' ' + objects() + ' ' + adverbs() + '?'

#отрицательных:
def negative1():
    return subjectscap() + ' ' + intrverbs() + ' ' + 'nicht' + '.'

def negative2():
    return subjectscap() + ' ' + trverbs() + ' ' + objects() + ' ' + 'nicht' + '.'

#выбираем случайный вариант для каждого типа предложения:
def random_affirmative():
    sentence = random.choice([1,2])
    if sentence == 1:
        return affirmative1()
    else:
        return affirmative2()

def random_incentive():
    sentence = random.choice([1,2])
    if sentence == 1:
        return incentive1()
    else:
        return incentive2()

def random_condition():
    sentence = random.choice([1,2])
    if sentence == 1:
        return condition1()
    else:
        return condition2()

def random_question():
    sentence = random.choice([1,2])
    if sentence == 1:
        return question1()
    else:
        return question2()

def random_negative():
    sentence = random.choice([1,2])
    if sentence == 1:
        return negative1()
    else:
        return negative2()
    
#наконец, задаём случайный порядок предложений:
final = [random_affirmative(), random_incentive(),random_condition(),random_question(), random_negative()]
random.shuffle(final)
final_str = str(final[0])
for s in final[1:]:
 final_str = final_str + ' ' + str(s)

print(final_str)

