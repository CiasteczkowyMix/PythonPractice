import re
import random
import tkinter
from tkinter import *
root = Tk()
root.title("Kryptograf")
root.geometry("250x170")
root.configure(bg="#00ffff")
def kill():
    root.destroy()
def encoding():
    button2.destroy()
    kontr = random.randint(10,99)
    a = code.get()
    root.mainloop()
    i=0
    global d
    d = ""
    test=((ord(a[i:i+1])*2-16)*4+8-(2*i*(i-1)))/2+kontr*(i+1)
    while i<len(a):
        m = ord(a[i:i+1])
        m = ((m*2-16)*4+8-(2*i*(i-1)))/2+kontr*(i+1)
        if i%2 == 0 and i !=0:
            m = m*4
        if i%3 == 0 and i != 0:
            m = m+16
        if i>0:
            m = (m*4 + test*2)/2 - 8
        d += str(int(m)) + " "
        i=i+1
    d=d[0:len(d)-1]
    d=d+ " " + str(kontr)+str(random.randint(0,9))+str(random.randint(0,9))
    global f
    f = 1 
def decode():
    txt2.grid()
    code.grid()
    txt4.grid()
    button.grid()
    button3.grid()
    txt.destroy()
    kod.destroy()
    dekod.destroy()
def encode():
    txt3.grid()
    code.grid()
    txt4.grid()
    button2.grid()
    button3.grid()
    txt.destroy()
    kod.destroy()
    dekod.destroy()
def decoding():
    button.destroy()
    s = code.get()
    root.mainloop()
    if s[len(s)-1:len(s)].isspace():
        s = s[0:len(s)-1]
    kontr = int(s[len(s)-4:len(s)-2])
    s = s[0:len(s)-5]
    s += " "
    i=0
    l=""
    global p
    p=""
    pl=0
    while i<len(s):
        while ord(s[i:i+1]) != 32:
            l += s[i:i+1]
            i = i+1
        m = int(l)
        if pl>0:
            m = ((m+8)*2-test*2)/4
        else:
            test=m
        if pl%3 == 0 and pl!=0:
            m=m-16
        if pl%2 == 0 and pl!=0:
            m = m/4 
        m = ((((m-kontr*(pl+1))*2-8+(2*pl*(pl-1)))/4+16)/2)
        p += chr(int(m))
        l = ""
        i=i+1
        pl=pl+1
    global f
    f = 0 
txt = Label(root, text="What you want?", bg="#00ffff")
txt2 = Label(root, text="Type code to decode:", bg="#00ffff")
txt3 = Label(root, text="Type text to encode:", bg="#00ffff")
txt4 = Label(root, text="Type coding method:", bg="#00ffff")
spacja = Label(root, text="                       ", bg="#00ffff")
kod = Button(root, text="encoding", command=encode, bg="#00fbff")
dekod = Button(root, text="decoding", command=decode, bg="#00fbff")
code = Entry(root, bg="aqua", fg="darkgreen", width = 40, borderwidth = 5)
button = Button(root, text="decode", command=decoding, bg="#00fbff")
button2 = Button(root, text="encode", command=encoding, bg="#00fbff")
button3 = Button(root, text="show answer", command=kill, bg="#00fbff")
k = "k"
while k == "k":
    spacja.grid(row=0, column=0)
    txt.grid(row=1, column=5)
    kod.grid(row=2, column=5)
    dekod.grid(row=3, column=5)
    root.mainloop()
    glowny = Tk()
    glowny.title("Answer")
    glowny.geometry("400x400")
    textbox = Text(glowny, width = 395, height = 395,bg="#ceffff")
    textbox.grid()
    if f==1:
        textbox.insert(END, d)
    if f==0:
        textbox.insert(END, p)
    glowny.mainloop()
    k = "q"