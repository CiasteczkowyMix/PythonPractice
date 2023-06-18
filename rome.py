ans = input("Which number do you want to convert?\n")
tys = ["","M","MM","MMM"]
sto = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
dzi = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
jed = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
outend = ""
while not ans.isnumeric() or (ans.isnumeric() and (int(ans) < 1 or int(ans) > 399903999)):
    ans = input("This must be an number!\n")
ans = int(ans)
if ans >= 4000 and ans < 399903999:
    if int(ans/100) < 4000:
        ans2 = int(ans/100)
        sign = 1
    elif int(ans/1000) < 4000:
        ans2 = int(ans/1000)
        sign = 2
    elif int(ans/100000) < 4000:
        ans2 = int(ans/100000)
        sign = 3
    else:
        print("ERROR")
    ms = int(ans2/1000)
    cs = int((ans2 - ms*1000)/100)
    xs = int((ans2 - ms*1000 - cs*100)/10)
    ii = int(ans2 - ms*1000 - cs*100 - xs*10)
    out = tys[ms] + sto[cs] + dzi[xs] + jed[ii]
    #Niedokończona implementacja liczba większych niż 4000
    match sign:
        case 1: 
            outend = "|"+out+"|"
            ans = str(ans)
            ans = ans[0:2]
            print("a")
        case 2: 
            i = len(out)
            top = ""
            while(i):
                top += "_"
                i -= 1
            print(top)
            outend = out
            ans = str(ans)
            ans = ans[0:3]
            print("b")
        case 3: 
            i = len(out) + 2
            top = ""
            while(i):
                top += "_"
                i -= 1
            print(top)
            outend = "|"+out+"|"
            ans = str(ans)
            ans = ans[0:5]
            print("c")
    print(ans)
    print(ans2)
ans = int(ans)
ms = int(ans/1000)
cs = int((ans - ms*1000)/100)
xs = int((ans - ms*1000 - cs*100)/10)
ii = int(ans - ms*1000 - cs*100 - xs*10)
outend += tys[ms] + sto[cs] + dzi[xs] + jed[ii]
print(outend)