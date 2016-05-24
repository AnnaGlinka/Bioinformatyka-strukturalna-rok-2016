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
                return
          
    #print(mapaWiazan)
    if len(stos):
        print("nieprawidlowe dane, za duzo nawiasow otwierajacych")
        return
  
    

    stos.clear()
   
    kropka = re.compile('[.]{1,1000}')
    st = re.compile('[()]{1,1000}')

    
    stosIterator = st.finditer(RNA_krn)
    
    for s in stosIterator:
        stos.append(s.span())

   

    kropkiIterator = kropka.finditer(RNA_krn)
    for kr in kropkiIterator:
        #print(kr)
        kropki.append(kr.span())
    #for kr in kropki:
     #   print("kropki", kr)

    for kr in kropki:
        poczatek = kr[0] #pierwszy z pary kropek
        koniec = kr[1] #drugi z pary kropek

        if poczatek == 0 or koniec>len(RNA_krn)-1:
            pojedynczyLancuch.append((poczatek,koniec-1))
            continue
       
        #for sp in spinkiDoWlosow:
         #   print("spinka", sp[0], sp[1])
        if (RNA_krn[poczatek-1]==')' and RNA_krn[koniec]=='('):
            #print("poczatek-1", poczatek-1, mapaWiazan.get(poczatek-1,  'None'))
            #print(mapaWiazan.get(3,  'None'))
            #print(kropki.index(a int table table, 5))
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
           
            #print("poczatek-1", poczatek-1, mapaWiazan.get(poczatek-1,  'None'))
            #print("koniec", koniec, mapaWiazan.get(koniec,  'None'))
            #petla.append((poczatek, koniec-1))
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
    
    '''
    print(RNA_kropkowo_nawiasowa)
    print("pojedynczy lancuch", pojedynczyLancuch)
    print("spinkiDoWlosow", spinkiDoWlosow)
    print("petla", petla)
    print("wybrzuszenie", wybrzuszenie)
    print("skrzyzowanie", skrzyzowanie)
    print("stos", stos)
    '''

    #for x in RNA_kropkowo_nawiasowa:
        
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
            #print("x in skrzyzowanie", x, ciag[ind+1][0], mapaWiazan.get(ciag[ind+1][0]))
            #print("x in skrzyzowanie drugi nawias", x, ciag[ind-1][1], mapaWiazan.get( ciag[ind-1][1]))
            stri += "x"*(x[1]-x[0]+1)
            #stri2 += "x"
            if ciag[ind+1][0] < mapaWiazan.get(ciag[ind+1][0]) and ciag[ind-1][1] > mapaWiazan.get( ciag[ind-1][1]):
                stri2 +="]x["
                #stri2 += "x"
                continue
            if ciag[ind-1][1] > mapaWiazan.get( ciag[ind-1][1]) and ciag[ind-1][1] > mapaWiazan.get( ciag[ind-1][1]):
                #stri2 += "x"
                stri2 +="]x"
                continue
            if ciag[ind-1][1] < mapaWiazan.get( ciag[ind-1][1]) and ciag[ind-1][1] < mapaWiazan.get( ciag[ind-1][1]):
                #stri2 += "x"
                stri2 +="x["
                continue

            continue
        else:
            stri += "d"*(x[1]-x[0]+1)
            #stri2 += "d"
            

    print(RNA_krn)
   
    print(stri2)
    print( stri)
    #print(mapaWiazan)

    #-----------------------
    

    return stri2, mapaWiazan
        

    

if __name__ == "__main__":

     #elementyStruktury('((([[..)))..]]')
     #elementyStruktury('......(((.{[[....[[)))...].].}.]]..')
     #elementyStruktury('.((((((..(((.....[....)))..((((.......))))......(((((..]....))))))))))).')
     #elementyStruktury('.((((((..(((....(((....)))...)))..((((.......))))......(((((..]....))))))))))).')
     #elementyStruktury('.((((((..((((....(((....)))...)))..((((.......))))......(((((..]....))))))))))).')
     #elementyStruktury('.((((((..(((....(((....)))...)))..((((.......)))))......(((((..]....))))))))))).')
     elementyStruktury('..((((...(((...)))..)))(((....(((...)))...)))...')
     #elementyStruktury('..(((...)))..')
     #elementyStruktury('....((((((..((((........)))).(((((.......)))))).....(((((.......))))))))))..')
     #elementyStruktury('..((((((...)))(((...)))(((...)))))).')
     #elementyStruktury('..((..(((..((..))..)))..))..')
     #elementyStruktury('..((..(((((..))..)))..))..')
     #elementyStruktury('..((..(((..((..)))))..))..')
     elementyStruktury('(((..(((...)))...(((...)))..)))')
     #drzewo 7
     elementyStruktury('((..((..((..((..((..((..((..))..((..((..((..))..))..))..))..))..))..((..))..((..((..((..((..((..))..))..((..((..))..))..))..))..))..((..((..((..((..))..((..))..))..))..))..))..))..))') 
     
     #elementyStruktury('..(((...(((.....))))))...')
     #elementyStruktury('((..((..((..))..((..))..))..((..))..))')

     #PDB_00547
     #c = elementyStruktury('..((((..(((((.(((((((((....)))))))))..)))))....((((((((....((((.(((((....))))).)))).)))))))).))))')
     #print(c)
    

    
     

#'((((((....)))....(((....))))))...'
#'..((((((...))).(((...))).(((...))))))'
#'..((((...(((...)))..)))(((....(((...)))...)))...'










































































































































































































































































































































































