import random
#генерит два массива, чет и нечет в 10 раз длиннее, уже отсортированных
def generate_fortest(leng):
    m1,m2=[],[]
    cur=0
    for i1 in range(leng):
        cur=cur+random.randint(0,1)*2
        m1.append(cur)
    cur=1
    for i2 in range(leng*10):
        cur=cur+random.randint(0,5)*2
        m2.append(cur)
    return [m1,m2]


#я игралась с разными видами генерации, графики с ними лежат в отдельной папке
#рандомные числа от 0 до 2000, списки отличаются в 1-3 раз
def generate_normal(leng):
    m1,m2=[],[]
    for i1 in range(leng): m1.append(random.randint(0,2000))
    for i1 in range(leng*random.randint(3,3)): m2.append(random.randint(0, 2000))
    return [sorted(m1),sorted(m2)]

#рандомные числа от 0 до 10000, списки отличаются в 1-3 раз, общих значений нет
def generate_nocommon(leng):
    m1, m2 = [], []
    for i1 in range(leng): m1.append(random.randint(0, 5000)*2)
    for i1 in range(leng * random.randint(3, 3)):
        x=random.randint(0, 5000)
        m2.append(x*2 +1)
    return [sorted(m1), sorted(m2)]

#рандомные числа от 0 до 2000, списки отличаются в 1-3 раз, много одинаковых значений
def generate_common(leng):
    m1, m2 = [], []
    for i1 in range(leng):
        elem=random.randint(0, 2000)
        for k1 in range(random.randint(0,10)):
            m1.append(elem)
    for i1 in range(leng * random.randint(3, 3)): m2.append(random.randint(0, 2000))
    return [sorted(m1), sorted(m2)]

#рандомные числа от 0 до 2000, списки отличаются в 10 раз
def generate_different_length(leng):
    m1, m2 = [], []
    for i1 in range(leng): m1.append(random.randint(0, 2000))
    for i1 in range(leng * 10): m2.append(random.randint(0, 2000))
    return [m1, m2]

#рандомные числа от 0 до 25000, списки отличаются в 1-3 раз
def generate_large_values(leng):
    m1, m2 = [], []
    for i1 in range(leng): m1.append(random.randint(0, 25000))
    for i1 in range(leng * random.randint(3, 3)): m2.append(random.randint(0, 25000))
    return [sorted(m1), sorted(m2)]

