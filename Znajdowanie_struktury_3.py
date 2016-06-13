import re

def elementyStruktury(RNA_kropkowo_nawiasowa):

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
    spinkaBezKr = []
    wybrzuszenieOdpowiednikZlewej = []
    skrzyzowanieBezKropek = []
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
    skrzyzowanie_bez_kropek = re.compile('[)][(]')

    skrzyzowanie_bez_kropekIterator = skrzyzowanie_bez_kropek.finditer(RNA_krn)
    for skbk in skrzyzowanie_bez_kropekIterator:
        skrzyzowanieBezKropek.append((skbk.span()))
        x = skbk.span()
     
    l = len(skrzyzowanieBezKropek)

    if l > 0:
        skrzyzowanieBezKropek.append((mapaWiazan.get(skrzyzowanieBezKropek[0][0]), mapaWiazan.get(skrzyzowanieBezKropek[0][0])))
        skrzyzowanieBezKropek.append((mapaWiazan.get(skrzyzowanieBezKropek[l-1][1]-1), mapaWiazan.get(skrzyzowanieBezKropek[l-1][1]-1)))
    
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
            #print("do wyb z prawej", mapaWiazan.get(poczatek-1,  'None'), mapaWiazan.get(koniec,  'None')  )
            if mapaWiazan.get(poczatek-1,  'None') -  mapaWiazan.get(koniec,  'None') == 1:
                wybrzuszenie.append((poczatek, koniec-1))
                wybrzuszenieOdpowiednikZlewej.append((mapaWiazan.get(koniec,  'None'), mapaWiazan.get(poczatek-1,  'None')))
            else:
                petla.append((poczatek, koniec-1))
            continue
    skrzyzowanieBezKropek.sort()
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
    # z - odpowiednik do wybrzuszenia pojawiajacego si� po prawej stronie
    # o - skrzyzowanie bez niesparowanych nukleotydow pomiedzy odgalezieniami
        
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
    for sbk in spinkaBezKr:
        ciag.append(sbk)
    for z in wybrzuszenieOdpowiednikZlewej:
        ciag.append(z)
    for skbk in skrzyzowanieBezKropek:
        ciag.append(skbk)
   

  
    ciag.sort()

    stri = ""
    stri2 = ""

    for ind, x in enumerate(ciag):

        if x in skrzyzowanieBezKropek:
           
            if mapaWiazan.get(x[0]) < x[0] and mapaWiazan.get(x[1]) > x[1]:
                 stri2 += "]["
            elif mapaWiazan.get(x[0]) > x[0]:
                stri2 += "["
            else:
                stri2+= "]"

            #stri2 += "o"
            continue
        if x in spinkaBezKr:
            stri2 += "r"
            continue
        if x in wybrzuszenieOdpowiednikZlewej:
            stri2 += "z"
            continue
        if x in pojedynczyLancuch:
            #print(len(x))
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
            #stri2 += "x"
            if ciag[ind+1][0] < mapaWiazan.get(ciag[ind+1][0]) and ciag[ind-1][1] > mapaWiazan.get( ciag[ind-1][1]):
                stri2 +="]["
                #stri2 += "x"
                continue
            if ciag[ind-1][1] > mapaWiazan.get( ciag[ind-1][1]) and ciag[ind-1][1] > mapaWiazan.get( ciag[ind-1][1]):
                #stri2 += "x"
                stri2 +="]"
                continue
            if ciag[ind-1][1] < mapaWiazan.get( ciag[ind-1][1]) and ciag[ind-1][1] < mapaWiazan.get( ciag[ind-1][1]):
                #stri2 += "x"
                stri2 +="["
                continue

            continue
        else:
            stri += "d"*(x[1]-x[0]+1)
            #stri2 += "d"
            

    print("RNA:  ", RNA_krn)
    print("stri: ", stri)
    print("stri2: ",stri2)
    
    print("----------------------------------------------")

    return stri2, mapaWiazan
        
if __name__ == "__main__":

     elementyStruktury('((([[..)))..]]')
     elementyStruktury('((..(())..))')
     elementyStruktury('(((((..(())..)))..))')
     elementyStruktury('......(((.{[[....[[)))...].].}.]]..')
     elementyStruktury('.((((((..(((.....[....)))..((((.......))))......(((((..]....)))))..)))))).')
     elementyStruktury('.((((((..(((....(((....)))...)))..((((.......))))......(((((..]....)))))..)))))).')
     elementyStruktury('..((((...(((..)))..)))(((....(((...)))...)))...')
     elementyStruktury('..((((..((..))..))((..((..))..))))...')
     elementyStruktury('..(((.((((((...)))....)))....)))')
     elementyStruktury('..((((((...)))(((...)))(((...)))(((...)))(((...)))(((...)))(((...)))))).')
     elementyStruktury('..((((((...)))(((...)))..(((...)))(((...)))(((...)))(((...)))(((...)))))).')
     elementyStruktury('..((((((...)))(((..((..(())..))..((..(())..))..)))..(((...)))(((...)))(((...)))(((...)))(((...)))))).')
     elementyStruktury('..(((((()))(((...)))(((...)))))).')
     elementyStruktury('..((..(((..((..))..)))..))..')
     elementyStruktury('..((..{(((((..))..))))..))..')
     elementyStruktury('..((..(((..((..)))))..))..')
     elementyStruktury('(((..(((...)))...(((...)))..)))')
     #drzewo 7
     elementyStruktury('((..((..((..((..((..((..((..))..((..((..((..))..))..))..))..))..))..((..))..((..((..((..((..((..))..))..((..((..))..))..))..))..))..((..((..((..((..))..((..))..))..))..))..))..))..))')
     #drzewo 7 z wybrzuszeniem
     elementyStruktury('((((((((..((((....((..((((..((..(((((.....)))))....(((((..((..((((....))))..))....)))))..)).....))..))..))....(((((....)))..))..((...((..((..((((((....((((....))))..))))))..((..((....))..))....))..))..))..((..((..((((..((((...))))..((((...))))..))))..))..))..))..))..))))))))......')  
    
    
     #elementyStruktury('..(((...(((.....))))))...')
     #elementyStruktury('((..((..((..))..((..))..))..((..))..))')
     #elementyStruktury('..((((..(((((.(((((((((....)))))))))..)))))....((((((((....((((.(((((....))))).)))).)))))))).))))')
     elementyStruktury('....(((((((..((((.....((.....((((..((..((((......))))..((..((..((((......))))..((..((..((((..(((((......)))))..((((((......))))))..))))..))..))..))..))..))..))..))..))..(((((.......)))))..((..((..((..((..((((.......))))..))..((..((((.....))))..))..))..))..))..((..((..((((..((((.....))))..((((.....))))..))))..))..))..((..(((((..(((((..(((......)))..(((((.....)))))..)))))..)))))..))..))..))..)))))))...')  
     #PDB_00547
     elementyStruktury('..((((..(((((.(((((((((....)))))))))..)))))....((((((((....((((.(((((....))))).)))).)))))))).))))')
     #PDB_00142
     elementyStruktury('((((((...((((((..)))))).))))))')
     # CRW_00552
     elementyStruktury('.((((((((((.....((((((((....(((((((.............))))..)))...)))))).)).(((((((..(((((((....)))))))..)))))))...)))))))))).')
    
     






