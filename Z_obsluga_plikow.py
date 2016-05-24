import re


def elementyStruktury(RNA_kropkowo_nawiasowa, indeks, wyjscie):
    RNA_krn = ""
    for x in RNA_kropkowo_nawiasowa:
        if x == '(' or x == ')' or x == '.':
            RNA_krn += x
        else:
            RNA_krn += '.'
          
    mapaWiazan = {}
    stos = []
    spinkiDoWlosow = []
    kropki = []
    pojedynczyLancuch = []
    petla = []
    wybrzuszenie = []
    skrzyzowanie = []
    ciag = []
    for i, j in enumerate(RNA_krn):
            mapaWiazan[i] = None
    for i, j in enumerate(RNA_krn):
        if j == '(':
            stos.append(i)
        if j == ')':
            if len(stos):
                para1 = stos.pop()
                para2 = i
                mapaWiazan[para1] = para2
                mapaWiazan[para2] = para1
            else:
                print("\nstruktura nr", indeks+1, ":")
                print("nieprawidlowe dane, za duzo nawiasow zamykajacych\n")
                wyj = ' '.join(['\nstruktura nr',  str(indeks+1), ':\n', 'nieprawidlowe dane, za duzo nawiasow zamykajacych\n'])
                wyjscie.write(wyj)
                return
    if len(stos):
        print("\nstruktura nr", indeks+1, ":")
        print("nieprawidlowe dane, za duzo nawiasow otwierajacych\n")
        wyj = ' '.join(['\nstruktura nr',  str(indeks+1), ':\n', 'nieprawidlowe dane, za duzo nawiasow otwierajacych\n'])
        wyjscie.write(wyj)
        return
    stos.clear()
    kropka = re.compile('[.]{1,1000}')
    st = re.compile('[()]{1,1000}')
    stosIterator = st.finditer(RNA_krn)
    for s in stosIterator:
        stos.append(s.span())
    kropkiIterator = kropka.finditer(RNA_krn)
    for kr in kropkiIterator:
        kropki.append(kr.span())
    for kr in kropki:
        poczatek = kr[0] #pierwszy z pary kropek
        koniec = kr[1] #drugi z pary kropek

        if poczatek == 0 or koniec>len(RNA_krn)-1:
            pojedynczyLancuch.append((poczatek,koniec-1))
            continue
        if (RNA_krn[poczatek-1]==')' and RNA_krn[koniec]=='('):
        
            skrzyzowanie.append((poczatek, koniec-1))
            continue

        if (RNA_krn[poczatek-1]=='(' and RNA_krn[koniec]==')') :
           spinkiDoWlosow.append((poczatek, koniec-1))
           continue
        if (RNA_krn[poczatek-1]=='(' and RNA_krn[koniec]=='(') :
            if mapaWiazan.get(poczatek-1,  'None') -  mapaWiazan.get(koniec,  'None') == 1:
                wybrzuszenie.append((poczatek, koniec-1))
            else:
                petla.append((poczatek, koniec-1))
            continue
        if (RNA_krn[poczatek-1]==')' and RNA_krn[koniec]==')'):
            if mapaWiazan.get(poczatek-1,  'None') -  mapaWiazan.get(koniec,  'None') == 1:
                wybrzuszenie.append((poczatek, koniec-1))
            else:
                petla.append((poczatek, koniec-1))
            continue

    for sk in skrzyzowanie:
        poczatek_sk = sk[0]
        koniec_sk = sk[1]
        poprzednie_sk = mapaWiazan.get(poczatek_sk-1,  'None') - 1
        for pet in petla:
            if pet[1] == poprzednie_sk:
                skrzyzowanie.append((pet[0],pet[1]))
                petla.remove((pet[0],pet[1]))

    skrzyzowanie.sort()
    
    for p in pojedynczyLancuch:
        ciag.append(p)
    for s in spinkiDoWlosow:
        ciag.append(s)
    for p in petla:
        ciag.append(p)
    for w in wybrzuszenie:
        ciag.append(w)
    for s in skrzyzowanie:
        ciag.append(s)
    for st in stos:
        ciag.append((st[0], st[1]-1))
   

  
    ciag.sort()

    stri = ""
    stri2 = ""

    for ind, x in enumerate(ciag):
        if x in pojedynczyLancuch:
            stri += "l"*(x[1]-x[0]+1)
            stri2 += "l"
            continue
        if x in spinkiDoWlosow:
            stri += "s"*(x[1]-x[0]+1)
            stri2 += "s"
            continue
        if x in petla:
            stri += "p"*(x[1]-x[0]+1)
            stri2 += "p"
            continue
        if x in wybrzuszenie:
            stri += "w"*(x[1]-x[0]+1)
            stri2 += "w"
            continue
        if x in skrzyzowanie:
            stri += "x"*(x[1]-x[0]+1)
            if ciag[ind+1][0] < mapaWiazan.get(ciag[ind+1][0]) and ciag[ind-1][1] > mapaWiazan.get( ciag[ind-1][1]):
                stri2 +="]x["
                continue
            if ciag[ind-1][1] > mapaWiazan.get( ciag[ind-1][1]) and ciag[ind-1][1] > mapaWiazan.get( ciag[ind-1][1]):
                stri2 +="]x"
                continue
            if ciag[ind-1][1] < mapaWiazan.get( ciag[ind-1][1]) and ciag[ind-1][1] < mapaWiazan.get( ciag[ind-1][1]):
                stri2 +="x["
                continue
            continue
        else:
            stri += "d"*(x[1]-x[0]+1)
            #stri2 += "d"
            
    print("\nstruktura nr", indeks+1, ":")
    print(RNA_krn)
    print( stri, "\n")
    wyj = ' '.join(['\nstruktura nr',  str(indeks+1), ':\n', str(RNA_krn), '\n', str(stri), '\n'])
    wyjscie.write(wyj)
    
    return stri2, mapaWiazan, stri
#-----------------------------------------------------------------------------------------------------
def metrykaHausdorffa(S1, S2):
    mapaS1 = {}
    stos = []
    for i, j in enumerate(S1):
            if j == '(':
                    stos.append(i)
            elif j == ')':
                    para1 = stos.pop()
                    para2 = i
                    mapaS1[para1] = para2
    mapaS2 = {}
    stos = []
    for i, j in enumerate(S2):
            if j == '(':
                    stos.append(i)
            elif j == ')':
                    para1 = stos.pop()
                    para2 = i
                    mapaS2[para1] = para2
                    
    print("mapaS1" , mapaS1)
    print("mapaS2", mapaS2)
  
    wie = len(mapaS1) + 1
    kol = len(mapaS2) + 1
    print("kol:", kol, "wie:", wie)

    Matrix = [[0 for i in range(kol)] for i in range(wie)]
    print(Matrix)
    i = 0
    j = 0   
    for keys,values in mapaS1.items():
        for keys2,values2 in mapaS2.items():
            Matrix[i][j] = max(abs(keys2 - keys), abs(values2 - values))
            j = j + 1
        i = i + 1
        j = 0
    print("po wypelnieniu")
    for i in range(0, wie):
        for j in range(0, kol):
            print( Matrix[i][j], end=" ")
        print("")


    for i in range(0, wie-1):
        minRz = Matrix[i][0]
        for j in range(0, kol-1):
            if Matrix[i][j] < minRz:
                minRz = Matrix[i][j]
            Matrix[i][kol-1] = minRz 
     
    
    for j in range(0, kol-1):
        minKol = Matrix[0][j]
        for i in range(0, wie-1):
            if Matrix[i][j] <  minKol:
                 minKol = Matrix[i][j]
            Matrix[wie-1][j] = minKol
          

    print("po sumowaniu")
    for i in range(0, wie):
        for j in range(0, kol):
            print(Matrix[i][j], end=" ")
        print("")

    MaxPoRzedach =  Matrix[0][kol-1]
    for i in range(1, wie-1):
        if Matrix[i][kol-1] > MaxPoRzedach:
            MaxPoRzedach = Matrix[i][kol-1]
    print("MaxPoRzedach ", MaxPoRzedach)

    MaxPoKolum = Matrix[wie-1][0];
    for j in range(1, kol-1):
        if Matrix[wie-1][j] > MaxPoKolum :
            MaxPoKolum  =  Matrix[wie-1][j];
    print("MaxPoKolum ",   MaxPoKolum )

    return max(MaxPoRzedach,MaxPoKolum);
    
#-----------------------------------------------------------------------------------------------------
def porownywacz(str1, nr1, str2, nr2):
    print("porownuje", nr1, str1 )
    print("z ", nr2, str2)
#-----------------------------------------------------------------------------------------------------
def utworzZbiorZPliku(sciezka):
    f = open(sciezka, "r")
    print(f.name)
    struktury = []
   
    for lin in f:
        struktury.append(lin)
        #print(lin)

    #print(struktury)
    return struktury

#-----------------------------------------------------------------------------------------------------
def porownajStruktury(zbior, wyjscie):
    #print(zbior)
    mapy = {}
    for ind, z in enumerate(zbior):
        #mapy.update({ind: elementyStruktury(z, ind)[1]})
       
        elemStruktWyjscie = elementyStruktury(z, ind, wyjscie)
        if elemStruktWyjscie: #jesli jest wyjscie
           print(elemStruktWyjscie[1])
        for ind2, z2 in enumerate(zbior):
            if(ind == ind2):
                continue
            #print(ind+1, z)
            #print(ind2+1, z2)
            #porownywacz(z, ind+1, z2, ind2+1)
           


if __name__ == "__main__":
    
    #wejscie
    sciezka1 = r"E:\Bioinfor_projekt\Struktury_kropkowo_nawiasowa.txt"
    sciezka2 = r"E:\Bioinfor_projekt\Struktury_kropkowo_nawiasowa2.txt"
    #wyjscie
    wyjscie = open(r"E:\Bioinfor_projekt\Raport.txt", "w")


    zbiorStr = utworzZbiorZPliku(sciezka2)

    porownajStruktury(zbiorStr, wyjscie)

    wyjscie.close()


  