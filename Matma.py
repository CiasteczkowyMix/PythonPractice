import matplotlib.pyplot as plt
import random
import math

i = 0
test = 0
sm = -9999 #Podstawa obliczenia osi y
sn = 9999 #Podstawa obliczenia osi y
maxim = 50 #największa wartość x 
minim = -49 #najmniejsza wartość x 
pkt = maxim - minim #ilosc punktów
if pkt < 0:
    pkt = -1*pkt
if minim < 0 or maxim < 0:
    pkt = pkt+1
osn = minim #Podstawa obliczenia osi x
osm = maxim #Podstawa obliczenia osi x
a = 4
b = 20
c = "n"
p = "n"     #-b/(2*a)
q = "n"       #-(b*b-4*a*c)/(4*a)
x1 = "n"
x2 = "n"
px = -3    #y = a(x-x1)(x-x2) = a(x2 - xx2 - xx1 +x1x2) = ax2 - axx2 - axx1 + ax1x2 = a*x*x - b = a*(x2 - x1) + c = a*x1*x2
py = -25
x = [0]*pkt 
y = [0]*pkt
while i < pkt: # wypisywanie argumentów
    x[i] = maxim
    maxim = maxim-1
    i = i+1
i = 0 
while i < pkt: #wzór na zbiór wartości
    while a == "n" or b == "n" or c == "n" or p == "n" or q == "n":
        if p == "n":
            if x1 != "n" and x2 != "n":
                p = (x1+x2)/2
            elif a != "n" and b != "n":
                p = -b/(2*a)
            elif c != "n" and q != "n" and a != "n":
                p = math.sqrt((c-q)/a)
        if q == "n":
            if b != "n" and a != "n" and c != "n":
                q = -(b*b-4*a*c)/(4*a)
            elif a != "n" and b != "n" and (x1 != "n" or x2 != "n"):
                if x1 != "n":
                    q = (x1*2*a+b)*(x1*2*a+b)/(-4*a)
                else:
                    q = (x2*2*a+b)*(x2*2*a+b)/(-4*a)
        if x1 == "n":
            if a != "n" and ((b != "n" and c != "n") or q != "n"):
                if q != "n":
                    print("a")
                    x1 = (-b-math.sqrt(-(q*4*a)))/(2*a)
                else:
                    x1 = (-b-math.sqrt(-(b*b-4*a*c)/(4*a)))/(2*a)
        if x2 == "n":
            if a != "n" and ((b != "n" and c != "n") or q != "n"):
                if q != "n":
                    print(b*b-4*a*c)
                    print(q)
                    #print(math.sqrt(q))
                    x2 = (-b+math.sqrt(-(q*4*a)))/(2*a)
                else:
                    x2 = (-b+math.sqrt(-(b*b-4*a*c)/(4*a)))/(2*a)
        if b == "n":
            if a != "n" and p != "n" and b == "n":
                b = -2*a*p
            elif a != "n" and x1 != "n" and x2 != "n":
                b = -a*(x2 + x1)
        if c == "n":
            if a != "n" and b != "n" and px != "n" and py != "n":
                c = py - (a*px*px + b*px)
            elif a != "n" and p != "n" and q != "n":
                c = a*p*p+q
            elif a != "n" and b != "n" and py != "n" and px != "n":
                c = y - b*x - a*x*x
            elif x1 != "n" and x2 != "n" and a != "n":
                c = x1*x2*a
        if a != "n" and p != "n" and q != "n" and py == "n":
            if px != "n":
                py = a*(px-p)*(px-p)+q
            elif py == "n" and px == "n":
                px = random.randint(osn,osm)
                py = a*(px-p)*(px-p)+q
        test = test+1
        if test > 4:
            break
            print("Zbyt mało danych")
    if q != "n" and p != "n":
        y[i] = a*(x[i]-p)*(x[i]-p)+q
    #elif b != "n" and c != "n":
    #    y[i] = a*x[i]*x[i]+x[i]*b+c
    if y[i] > sm:
            sm = y[i]
    if y[i] < sn:
        sn = y[i]
    i=i+1
print("a=",a)
print("b=",b)
print("c=",c)
print("p=",p)
print("q=",q)
print("x1=",x1)
print("x2=",x2)
print("Przykładowy x=",px)
print("Przykładowe y=",py)
#funkcja = x*3+4
plt.plot(x,y)
plt.plot([osm+20,osn-20],[0,0])
plt.plot([0,0],[sn-20,sm+20])
plt.show()