import webbrowser
import os
if(os.path.isfile('strona2.html') == True):
    os.remove("strona2.html")
title = input("Choose title\n")
ts = ""
txt = ""
f2 = open("strona2.html", "x")
f2.close()
c = input("Czy chcesz dodać style? T/N\n")
if c == "T" or c == "t":
    wybor = input("Wybierz czy chcesz załączyć plik, czy stworzyć nowy\n(Nowy/Zał)\n")
    if wybor == "Nowy" or wybor == "nowy":
        if(os.path.isfile('kod.css') == True):
            os.remove("kod.css")
        kk = open("kod.css", "x")
        kk.close()
        kk = open("kod.css", "a", encoding="utf-8")
        kk.write("*{\n")
        kk.write("color:" + input("Wybierz color czcionki\n") +";\n")
        kk.write("font-size:" + input("Wybierz wielkość czcionki w px\n") + "px;\n")
        kk.write("background-color:" + input("Wybierz kolor tła\n") + ";\n")
        kk.write("font-family:" + input("Wybierz rodzaj czcionki\n") + ", Arial, sans-serif;")
        kk.write("}\n")
        kk.close()
        kod = "kod.css"
    else:
        kod = input("Wpisz nazwę bez rozszerzenia\n") + ".css"
else:
    kod = " "
answ = "Tak"
while answ == "Tak" or answ == "tak":
    f2 = open("strona2.html", "a", encoding="utf-8")
    ans = input("Gotowiec, czy własny kod?\n")
    if ans == "Gotowiec" or ans == "gotowiec":
        opcja = input("Wybierz szablon(lista/tabela)\n")
        if opcja == "Lista" or opcja == "lista":
        
            f = open("lista.txt", "r", encoding="utf-8")
    
            count = 0
            for line in f:

                if line != "\n":

                 count += 1
         
            f.close()
            f = open("lista.txt", "r", encoding="utf-8")
            i = 0
            t = []
            while i < count+2:
                t += f.readlines(i)
                i+=1
            f.close()

            i = 0
            lo = input("Lista uporządkowana, czy nieuporządkowana?(U/N)\n")
            if lo == "U" or lo == "u":
                l = "<ol>\n"
                while i < count-1:
                    k = t[i]
                    l+="<li>" + k[:-1] + "</li>\n"
                    i+=1
                k = t[i]
                l += "<li>" + k + "</li>\n"
                l +="</ol>"
            else:
                l = "<ul>\n"
                while i < count-1:
                    k = t[i]
                    l+="<li>" + k[:-1] + "</li>\n"
                    i+=1
                k = t[i]
                l += "<li>" + k + "</li>\n"
                l +="</ul>"
            txt += l
  
        if opcja == "tabela" or opcja == "Tabela":
            tr = int(input("Podaj ilość wierszy\n"))
            td = int(input("Podaj ilość kolumn\n"))    
            f = open("lista.txt", "r", encoding="utf-8")
    
            count = 0
            for line in f:

                if line != "\n":

                 count += 1
   
            f.close()
            if count != tr*td:
                print("błąd. Zła ilość rekordów")
                exit()
            f = open("lista.txt", "r", encoding="utf-8")
            i = 0
            t = []
            while i < count+2:
                t += f.readlines(i)
                i+=1
            f.close()

            l = "<table>"
            iv = 0
            ii = 0
            while ii < tr-1:
                l += "<tr>"
                iii = 0
                while iii < td:
                    k=t[iv]
                    l += "<td>"+k[:-1]+"</td>"
                    iii += 1
                    iv += 1
                l += "</tr>"
                ii += 1
            iii = 0
            l += "<tr>"
            while iii < td-1:
                k=t[iv]
                l += "<td>"+k[:-1]+"</td>"
                iii += 1
                iv += 1
            k=t[iv]
            l += "<td>"+ k + "</td></tr>"
            l += "</table>"
            txt += l
            ta = input("Czy chcesz stylować tabele?(Tak/Nie)\n")
            if ta == "Tak" or ta == "tak":
                tc = input("Wybierz kolor tekstu\n")
                tc2 = input("Wybierz kolor obramowania\n")
                st = input("Podaj szerokosc w pikselach\n")
                rt = input("Podaj rodzaj obramowania(np dashed/dotted/solid)\n")
                btk = input("Podaj kolor tla\n")
                ts = "<style> table, th, td {border: " + st + "px " + rt + " " + tc2 + "; border-collapse: collapse; color: " + tc + "; background-color: "+ btk + "}</style>\n"
    else:
        f = open("strona.txt", "r", encoding="utf-8")
        txt += f.read()
        f.close()
    answ = input("Czy chcesz jeszcze cos dodac?(Tak/Nie)\n")
 

f2.write("<!DOCTYPE html>\n<html>\n<head>\n<title>"+ title +"</title><meta charset='utf-8'><link rel='stylesheet' href='" + kod + "'>" + ts + "</head>\n<body>\n")
f2.write(txt)
f2.write("\n</body>\n</html>")

webbrowser.open("strona2.html")
f2.close()