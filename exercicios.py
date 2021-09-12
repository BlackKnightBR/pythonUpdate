import math

def sen(a):
    a += - (a ** 3 / 6 ) + (a ** 5 / 120) - (a ** 7 / 5040)
    return a

def tabela():
    x = 0.0
    while ( x <= 6.3):
        print("Sen: {} em Graus {}".format(x,sen(x)))
        x += 0.1
def pi():
    quatro = 4.0
    pi = 4.0
    x = 3.0
    mult = -1.0
    teste =  (quatro/x)
    while(teste >= 0.0001):
        pi += mult * teste
        mult *= -1.0
        x += 2
        teste =  (quatro/x)
    return pi

def pi2():
    quatro = 4.0
    pi = 4.0
    x = 3.0
    mult = -1.0
    teste =  (quatro/x)
    while(teste >= 0.00001):
        pi += mult * teste
        mult *= -1.0
        x += 2
        teste =  (quatro/x)
    return pi

def read(x):
    mult = 1.0
    teste =  1
    exp = 25
    final = 0.0
    while(teste <= 25):
        final += mult * (float(x) ** exp / teste)
        mult *= -1.0
        teste += 1
        exp -= 1
    return final

def s():
    s = 0
    mult = 1.0
    denom = 1
    nume = 225
    decre = 29
    while (denom <= 16384):
        s += mult * (denom / nume)
        denom *= 2
        mult *= -1.0
        nume -= decre
        decre -= 2
    return s

def loop():
    cem = 100
    s = 0
    for i in range(20):
        s += cem/fat(i)
        cem -= 1
    return s

def fat(x):
    fat = 1
    while( x > 0):
        fat *= x
        x -= 1
    return fat

def loop2():
    cem = 61
    s = 63
    cont = 1
    soma = cem / fat(cont)
    while soma > 0.000001:
        s += soma
        cem -= 2
        cont += 1
        soma = cem / fat(cont)
    return "Somatório é: {} e foram precisas {} iterações.".format(s,cont)

def loop3():
    cem = 100
    s = 0
    mult = 1.0
    for i in range(51):
        if(i > 0):
            s += mult * fat(i)/ i
            mult *= -1
    return s

def expe(x):
    e = 1
    expo  = round(math.exp(x),5)
    count = 1
    while count <= 50:
        e +=  (x ** count) / fat(count)
        count += 1
    return e

def som2(x):
    s = x
    mult = 1.0
    for i in range(21):
        if(i > 0):
            s += x ** (i+1)/ fat(i+2)
            mult *= -1
    return s

print(som2(2))
