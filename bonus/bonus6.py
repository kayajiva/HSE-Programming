height = float(input("Рост в сантиметрах: "))
weight = float(input("Масса тела в килограммах: "))
ind = weight / ((height/100) **2)
if ind <= 16:
    print("Выраженный дефицит массы тела")
elif ind > 16 and ind <= 18.5:
    print("Недостаточная масса тела")
elif ind > 18.5 and ind <= 24.99:
    print("Норма")
elif ind >= 25 and ind <= 30:
    print("Ожирение первой степени")
elif ind > 30 and ind <=40:
    print("Ожирение второй степени")
elif ind > 40:
    print("Ожирение третьей степени")
             
