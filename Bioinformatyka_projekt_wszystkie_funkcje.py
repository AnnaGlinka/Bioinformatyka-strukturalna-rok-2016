import re
import numpy as np

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
    ciagDoBudowyDrzewa = []
    spinkaBezKr = []
    wybrzuszenieOdpowiednikZlewej = []
    skrzyzowanieZiBezKropek = []
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
                print("nieprawidlowe dane, za duzo nawiasow zamykajacych")
                print("--------------------------------------------------")
                return
          
    
    if len(stos):
        print("nieprawidlowe dane, za duzo nawiasow otwierajacych")
        print("--------------------------------------------------")
        return
  
    stos.clear()
    kropka = re.compile('[.]{1,1000}')
    st = re.compile('[()]{1,1000}')
    spinka_bez_kropek = re.compile('[(][)]')
    skrzyzowanie_z_i_bez_kropek = re.compile('[)][.]{0,1000}[(]')

    skrzyzowanie_z_i_bez_kropekIterator = skrzyzowanie_z_i_bez_kropek.finditer(RNA_krn)
    for skbk in skrzyzowanie_z_i_bez_kropekIterator:
        skrzyzowanieZiBezKropek.append((skbk.span()))
        x = skbk.span()
        skrzyzowanieZiBezKropek.append( (mapaWiazan.get(x[0]),  mapaWiazan.get( x[0])) )
        skrzyzowanieZiBezKropek.append( (mapaWiazan.get(x[1]),  mapaWiazan.get( x[1])) )

     
    l = len(skrzyzowanieZiBezKropek)

  
    spinka_bez_kropekIterator = spinka_bez_kropek.finditer(RNA_krn);
    for sbk in spinka_bez_kropekIterator:
        spinkaBezKr.append(sbk.span());

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
                wybrzuszenieOdpowiednikZlewej.append((mapaWiazan.get(koniec,  'None'), mapaWiazan.get(poczatek-1,  'None')))
            else:
                petla.append((poczatek, koniec-1))
            continue
    skrzyzowanieZiBezKropek.sort()
    for sk in skrzyzowanie:
        poczatek_sk = sk[0]
        koniec_sk = sk[1]
        poprzednie_sk = mapaWiazan.get(poczatek_sk-1,  'None') - 1
        for pet in petla:
            if pet[1] == poprzednie_sk:
                skrzyzowanie.append((pet[0],pet[1]))
                petla.remove((pet[0],pet[1]))

    skrzyzowanie.sort()
    
   
    # r - oznaczenie jak dla spinki do wlosow, ale bez niesparowanych nukleotydow ((()))
    # z - odpowiednik do wybrzuszenia pojawiajacego si? po prawej stronie
    # o - skrzyzowanie bez niesparowanych nukleotydow pomiedzy odgalezieniami
        
    for p in pojedynczyLancuch:
        ciag.append(p)
        ciagDoBudowyDrzewa.append(p)
    for s in spinkiDoWlosow:
        ciag.append(s)
        ciagDoBudowyDrzewa.append(s)
    for p in petla:
        ciag.append(p)
        ciagDoBudowyDrzewa.append(p)
    for w in wybrzuszenie:
        ciag.append(w)
        ciagDoBudowyDrzewa.append(w)
    for s in skrzyzowanie:
        ciag.append(s)
    for st in stos:
        ciag.append((st[0], st[1]-1))
        ciagDoBudowyDrzewa.append((st[0], st[1]-1))
    for sbk in spinkaBezKr:
        ciagDoBudowyDrzewa.append(sbk)
    for z in wybrzuszenieOdpowiednikZlewej:
        ciagDoBudowyDrzewa.append(z)
    for skbk in skrzyzowanieZiBezKropek:
        ciagDoBudowyDrzewa.append(skbk)
   

  
    ciag.sort()
    ciagDoBudowyDrzewa.sort()

    stri = ""
    stri2 = ""

    for ind, x in enumerate(ciag):
        if x in pojedynczyLancuch:
            stri += "l"*(x[1]-x[0]+1)
            continue
        if x in spinkiDoWlosow:
            stri += "s"*(x[1]-x[0]+1)
            continue
        if x in petla:
            stri += "p"*(x[1]-x[0]+1)
            continue
        if x in wybrzuszenie:
            stri += "w"*(x[1]-x[0]+1)
            continue
        if x in skrzyzowanie:
            stri += "x"*(x[1]-x[0]+1)
           
            continue
        else:
            stri += "d"*(x[1]-x[0]+1)

    for ind, x in enumerate(ciagDoBudowyDrzewa):

        if x in skrzyzowanieZiBezKropek:

         
           
            if mapaWiazan.get(x[0]) < x[0] and mapaWiazan.get(x[1]) > x[1]:
                 stri2 += "]["
            elif mapaWiazan.get(x[0]) > x[0]:
                stri2 += "["
            else:
                stri2+= "]"

            continue
        if x in spinkaBezKr:
            stri2 += "r"
            continue
        if x in wybrzuszenieOdpowiednikZlewej:
            stri2 += "z"
            continue
        if x in pojedynczyLancuch:
            #print(len(x))
            stri2 += "l"
            continue
        if x in spinkiDoWlosow:
            stri2 += "s"
            continue
        if x in petla:
            stri2 += "p"
            continue
        if x in wybrzuszenie:
            stri2 += "w"
            continue

            
    print("\nstruktura nr", indeks+1, ":")
    print(RNA_krn)
    print( stri, "\n")
    print( stri2, "\n")
    wyj = ' '.join(['\nstruktura nr',  str(indeks+1), ':\n', str(RNA_krn), '\n', str(stri), '\n', str(stri2), '\n'])
    wyjscie.write(wyj)
    
    return stri2, mapaWiazan, stri
#-----------------------------------------------------------------------------------------------------
def drzewoDFS(elem):
    #print("wejscie: ", elem)
  
    i = 0
    wyjscie = ""   
    stos = []
    stosGalezi = []
    licznikNawiasow = 0 #zlicza ile razy stos nawiasow stal sie pusty
    galaz = ""
    
    if (elem[0] == 'l' or elem[-1] == 'l'):
        wyjscie+='1'

    while i < len(elem):
        
        if (elem[i] == 'p' or elem[i] == 'w' or elem[i] == 'z'):
                wyjscie+='1'
        if (elem[i] == 's' or elem[i] =='r'):
            wyjscie+='0'
            while elem[i] != ']' and i < len(elem)-1:
               i +=1

        elif (elem[i] == '['):
            while i < len(elem):
                if elem[i] == ']':
                    licznikNawiasow -=1
                if elem[i] == '[':
                    licznikNawiasow +=1
                galaz += elem[i]

                if licznikNawiasow == 0:
                    if len(galaz) > 1:
                        while galaz[0] == "[" or galaz[-1] == "]" and len(galaz)>0:
                            if galaz[0] == "[":
                               galaz = galaz[1:]
                            if galaz[-1] == "]":
                               galaz =  galaz[:-1]
                        stosGalezi.append(galaz)
                    galaz = ""
                i+=1


        if len(stosGalezi):
           licznikStosu = len(stosGalezi)
           wyjscie+=str(licznikStosu)

        while stosGalezi:
            e = stosGalezi.pop()

            ind = 0
            licznikNawiasow = 0
            licznikStosu2 = 0
            
            while ind < len(e):
               if (e[ind] == 'p' or e[ind] == 'w' or e[ind] == 'z'):
                   wyjscie+='1'
                  
               if (e[ind] == 's' or e[ind] =='r'):
                  wyjscie+='0'
                 
                  while e[ind] != ']' and ind < len(e)-1:
                      ind +=1

               elif (e[ind] == '['):
                   while ind < len(e):
                       if e[ind] == ']':
                           licznikNawiasow -=1
                       if e[ind] == '[':
                           licznikNawiasow +=1
       
                       galaz += e[ind]
                       if licznikNawiasow == 0:
                          if len(galaz) > 1:
                            stosGalezi.append(galaz[1:-1])
                            licznikStosu2 +=1
                          galaz = ""
                       ind+=1
               ind+=1
            if licznikStosu2 != 0:
                wyjscie+=str(licznikStosu2)
             
        i +=1

    return wyjscie
#-----------------------------------------------------------------------------------------------------
punktacja = {'dopasowanie':1, 'niedopasowanie':-1, 'przerwa':-1}

def sprawdzDopasowanie(x, y):
    if x == y:
        return punktacja['dopasowanie']
    elif x == "-" or y == "-":
        return punktacja['przerwa']
    else:
        return punktacja['niedopasowanie']

def NeedlemanWunsch(seq1, seq2, wyjscie):
    m, n = len(seq1), len(seq2)
    punkty = np.zeros((m+1, n+1))  
 # Faza inicjalizacji macierzy---------------------------------------------------------
    for i in range(m+1):
        punkty[i][0] = punktacja['przerwa'] * i
    for j in range(n+1):
        punkty[0][j] = punktacja['przerwa'] * j
 # Wypelnienie macierzy punktacji-------------------------------------------------------
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            przek = punkty[i-1][j-1] + sprawdzDopasowanie(seq1[i-1], seq2[j-1])
            D = punkty[i-1][j] + punktacja['przerwa']
            I = punkty[i][j-1] + punktacja['przerwa']
            punkty[i][j] = max(przek, D, I)
    i = m
    j = n
    dopasowanie_1 = "" 
    dopasowanie_2 = ""
 # Przejscie przez macierz-----------------------------------------------------------
    while (i>0 and j>0):
        punkty_teraz = punkty[i][j]
        punkty_przek = punkty[i-1][j-1]
        punkty_L = punkty[i][j-1]
        punkty_gora = punkty[i-1][j]
       
        if punkty_teraz == punkty_przek + sprawdzDopasowanie(seq1[i-1], seq2[j-1]):
            dop_1 = seq1[i-1]
            dop_2 = seq2[j-1]
            i = i-1
            j = j-1
        elif punkty_teraz == punkty_gora + punktacja['przerwa']:
            dop_1 = seq1[i-1]
            dop_2 = "-"
            i -= 1
        elif punkty_teraz == punkty_L + punktacja['przerwa']:
            dop_1 = "-"
            dop_2 = seq2[j-1]
            j -= 1
        dopasowanie_1+=dop_1
        dopasowanie_2+=dop_2
            
    while i>0:
        dop_1 = seq1[i-1]
        dop_2 = "-"
        dopasowanie_1+=dop_1
        dopasowanie_2+=dop_2
        i -= 1
    while j>0:
        dop_1 = "-"
        dop_2 = seq2[j-1]
        dopasowanie_1+=dop_1
        dopasowanie_2+=dop_2
        j -= 1
    
    dopasowanie_1 = dopasowanie_1[::-1]
    dopasowanie_2 = dopasowanie_2[::-1]
    sekwencja = len(dopasowanie_1)
    punktacjaSekwencji = 0
    identycznosc = 0
    for i in range(sekwencja):
        dop_1 = dopasowanie_1[i]
        dop_2 = dopasowanie_2[i]
        if dop_1 == dop_2:
            identycznosc += 1
            punktacjaSekwencji += sprawdzDopasowanie(dop_1, dop_2)
        else: 
            punktacjaSekwencji += sprawdzDopasowanie(dop_1, dop_2)
        
    identycznosc = identycznosc/sekwencja * 100
    wyj = ' '.join(['Metryka "drzewa" => po dopasowaniu', '\nsekwencja 1:',  str(dopasowanie_1), '\nsekwencja 2:', str(dopasowanie_2), '\nProcent identycznosci:', str(identycznosc), '\nPunktacja:', str(punktacjaSekwencji), '\n'])
    wyjscie.write(wyj)

    print("Po dopasowaniu")
    print("sekwencja 1:",dopasowanie_1)
    print("sekwencja 2:",dopasowanie_2)
    print("Procent identycznosci: %2.1f" % identycznosc)
    print("Punktacja:", punktacjaSekwencji)
    print()
    return identycznosc
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
                    
    wie = len(mapaS1) + 1
    kol = len(mapaS2) + 1
  
    Matrix = [[0 for i in range(kol)] for i in range(wie)]

    i = 0
    j = 0   
    for keys,values in mapaS1.items():
        for keys2,values2 in mapaS2.items():
            Matrix[i][j] = max(abs(keys2 - keys), abs(values2 - values))
            j = j + 1
        i = i + 1
        j = 0
   
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
    MaxPoRzedach =  Matrix[0][kol-1]
    for i in range(1, wie-1):
        if Matrix[i][kol-1] > MaxPoRzedach:
            MaxPoRzedach = Matrix[i][kol-1]
  
    MaxPoKolum = Matrix[wie-1][0];
    for j in range(1, kol-1):
        if Matrix[wie-1][j] > MaxPoKolum :
            MaxPoKolum  =  Matrix[wie-1][j];
    return max(MaxPoRzedach,MaxPoKolum);
    
#-----------------------------------------------------------------------------------------------------
def metrykaGory(S1, S2):
    vS1 = []
    vS2 = []
    S1c = 0
    S2c = 0

    for j in S1:
            if j == '(': 
                S1c+=1
                vS1.append(S1c)
            elif j == ')':
                S1c-=1
                vS1.append(S1c)
            else:
                vS1.append(S1c)

    for j in S2:
            if j == '(': 
                S2c+=1
                vS2.append(S2c)
            elif j == ')':
                S2c-=1
                vS2.append(S2c)
            else:
                vS2.append(S2c)

    return abs(sum(vS1)-sum(vS2))
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
           #print( elemStruktWyjscie[0])
           dfs = (drzewoDFS(elemStruktWyjscie[0]))
           print(dfs)
           wyj = ' '.join(['przeszukiwanie dfs:',  str(dfs), '\n'])
           wyjscie.write(wyj)

           mapy.update({ind: elemStruktWyjscie[1]})
        else:
            mapy.update({ind: None})
     
    wyj = "-------Porownywanie sekwencji--------------------------"
    wyjscie.write(wyj)
          
    for ind, z in enumerate(zbior):
        for ind2, z2 in enumerate(zbior):

           
            if ind == ind2:
                continue
            #print(mapy.get(ind))
            if mapy.get(ind) == None or mapy.get(ind2) == None:
                #print("None")
                continue

            #----------------------
            elemStruktWyjscie_z = elementyStruktury(z, ind, wyjscie)
            elemStruktWyjscie_z2 = elementyStruktury(z2, ind2, wyjscie)
            dfs_z = (drzewoDFS(elemStruktWyjscie_z[0]))
            dfs_z2 = (drzewoDFS(elemStruktWyjscie_z2[0]))



            #----------------------

            print("odleglosc struktury", ind+1, "od struktury", ind2+1, "wynosi")
            print("metryka Hausdorffa:", metrykaHausdorffa(z, z2))
            print("metryka gory:", metrykaGory(z, z2))
            print("metryka drzewa:")
            #NeedlemanWunsch(dfs_z, dfs_z2, wyjscie)
           

            wyj = ' '.join(['\nodleglosc struktury',  str(ind+1), 'od struktury', str(ind2+1), 'wynosi\n', 'metryka Hausdorffa:', str(metrykaHausdorffa(z, z2)), '\n', 'metryka gory:', str(metrykaGory(z, z2)), '\n', 'metryka drzewa - procent identycznosci:', str(NeedlemanWunsch(dfs_z, dfs_z2, wyjscie)), '\n'])
            wyjscie.write(wyj)
            
if __name__ == "__main__":
    
    #wejscie
    sciezka1 = r"E:\Bioinfor_projekt\Struktury_kropkowo_nawiasowa.txt"
    sciezka2 = r"E:\Bioinfor_projekt\Struktury_kropkowo_nawiasowa2.txt"
    sciezka3 = r"E:\Bioinfor_projekt\Struktury_kropkowo_nawiasowa3.txt"
    sciezka4 = r"E:\Bioinfor_projekt\Struktury_kropkowo_nawiasowa4.txt"
    sciezka5 = r"E:\Bioinfor_projekt\Struktury_kropkowo_nawiasowa5.txt"
    #wyjscie
  
    wyjscie = open(r"E:\Bioinfor_projekt\Raport1.txt", "w")
    

    zbiorStr = utworzZbiorZPliku(sciezka5)
    porownajStruktury(zbiorStr, wyjscie)
    wyjscie.close()


  