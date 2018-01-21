import random

#открываем файлы, достаём случайные слова: 
def subjects():
    with open('E:/random_deutsch/subjects.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

def subjectscap():
    with open('E:/random_deutsch/subjectscap.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

def objects():
    with open('E:/random_deutsch/objects.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)
 
def intrverbs():
    with open('E:/random_deutsch/intr_verbs.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

def intrverbscap():
    with open('E:/random_deutsch/intr_verbscap.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

def trverbs():
    with open('E:/random_deutsch/tr_verbs.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

def trverbscap():
    with open('E:/random_deutsch/tr_verbscap.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

def impintr2():
    with open('E:/random_deutsch/impintr2.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

def impintr3():
    with open('E:/random_deutsch/impintr3.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

def imptr2():
    with open('E:/random_deutsch/imptr2.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

def imptr3():
    with open('E:/random_deutsch/imptr3.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

def adverbs():
    with open('E:/random_deutsch/adverbs.txt', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\ufeff", "")
    text = text.split(';')
    return random.choice(text)

#теперь составляем из случайных слов 5 типов предложений
#в каждом типе будет несколько вариантов

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
    
#наконец, выбираем случайный порядок предложений:
final = [random_affirmative(), random_incentive(),random_condition(),random_question(), random_negative()]
random.shuffle(final)
final_str = str(final[0])
for s in final[1:]:
 final_str = final_str + ' ' + str(s)

print(final_str)

