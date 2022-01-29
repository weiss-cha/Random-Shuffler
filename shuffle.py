import random

def students2():
    list1 = []
    num = int(input('how many students?'))
    for i in range(1, num + 1):
        list1.append(i)
        i = i + 1
    random.shuffle(list1)
    print(list1)
