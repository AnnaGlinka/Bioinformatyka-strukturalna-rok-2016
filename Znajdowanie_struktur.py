import re


def elementyStruktury(RNA_kropkowo_nawiasowa):
    mapaWiazan = {}
    stos = []
    spinkiDoWlosow = []
    kropki = []
    pojedynczyLancuch = []
    petla = []
    wybrzuszenie = []
    skrzyzowanie = []
    ciag = []
    for i, j in enumerate(RNA_kropkowo_nawiasowa):
            mapaWiazan[i] = None
    for i, j in enumerate(RNA_kropkowo_nawiasowa):
        if j == '(':
            stos.append(i)
        if j == ')':
            para1 = stos.pop()
            para2 = i
            mapaWiazan[para1] = para2
            mapaWiazan[para2] = para1
          

    print(mapaWiazan)

    stos.clear()
   
    kropka = re.compile('[.]{1,1000}')
    st = re.compile('[(]{1,1000}')

    
    stosIterator = st.finditer(RNA_kropkowo_nawiasowa)
    
    for s in stosIterator:
        stos.append(s.span())

    #for s in stos:
        #print(s[0], s[1])

   
    

    kropkiIterator = kropka.finditer(RNA_kropkowo_nawiasowa)
    for kr in kropkiIterator:
        #print(kr)
        kropki.append(kr.span())
    #for kr in kropki:
     #   print("kropki", kr)

    for kr in kropki:
        poczatek = kr[0] #pierwszy z pary kropek
        koniec = kr[1] #drugi z pary kropek

        if poczatek == 0 or koniec>len(RNA_kropkowo_nawiasowa)-1:
            pojedynczyLancuch.append((poczatek,koniec-1))
            continue
       
        #for sp in spinkiDoWlosow:
         #   print("spinka", sp[0], sp[1])
        if (RNA_kropkowo_nawiasowa[poczatek-1]==')' and RNA_kropkowo_nawiasowa[koniec]=='('):
            #print("poczatek-1", poczatek-1, mapaWiazan.get(poczatek-1,  'None'))
            #print(mapaWiazan.get(3,  'None'))
            #print(kropki.index(a int table table, 5))
            skrzyzowanie.append((poczatek, koniec-1))
            continue

       
        
        if (RNA_kropkowo_nawiasowa[poczatek-1]=='(' and RNA_kropkowo_nawiasowa[koniec]==')') :
           spinkiDoWlosow.append((poczatek, koniec-1))
           continue
           
           
        if (RNA_kropkowo_nawiasowa[poczatek-1]=='(' and RNA_kropkowo_nawiasowa[koniec]=='(') :
            if mapaWiazan.get(poczatek-1,  'None') -  mapaWiazan.get(koniec,  'None') == 1:
                wybrzuszenie.append((poczatek, koniec-1))
            else:
                petla.append((poczatek, koniec-1))
           
            #print("poczatek-1", poczatek-1, mapaWiazan.get(poczatek-1,  'None'))
            #print("koniec", koniec, mapaWiazan.get(koniec,  'None'))
            #petla.append((poczatek, koniec-1))
            continue
        if (RNA_kropkowo_nawiasowa[poczatek-1]==')' and RNA_kropkowo_nawiasowa[koniec]==')'):
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
    
    print(RNA_kropkowo_nawiasowa)
    print("pojedynczy lancuch", pojedynczyLancuch)
    print("spinkiDoWlosow", spinkiDoWlosow)
    print("petla", petla)
    print("wybrzuszenie", wybrzuszenie)
    print("skrzyzowanie", skrzyzowanie)
    print("stos", stos)

    #for x in RNA_kropkowo_nawiasowa:
        

    ciag.append(pojedynczyLancuch)
    ciag.append(spinkiDoWlosow)
    ciag.append(petla)
    ciag.append(wybrzuszenie)
    ciag.append(skrzyzowanie)
    #ciag.append(stos)
    ciag.sort()
    print("ciag", ciag)

    stri = ""

    
    
    





if __name__ == "__main__":
 
     #elementyStruktury('..((((...(((...)))..)))(((....(((...)))...)))...')
     #elementyStruktury('..(((...)))..')
     #elementyStruktury('....((((((..((((........)))).(((((.......)))))).....(((((.......))))))))))..')
     #elementyStruktury('..((((((...)))(((...)))(((...)))))).')
     elementyStruktury('..((..(((..((..))..)))..))..')
     print("druga")
     #elementyStruktury('..((..(((((..))..)))..))..')
     #elementyStruktury('..((..(((..((..)))))..))..')
     elementyStruktury('(((..(((...)))...(((...)))..)))')
    # elementyStruktury('..(((...(((.....))))))...')
    # elementyStruktury('(((((((((...((((((.........))))))........((((((.......))))))..)))))))))')
    

     

#'((((((....)))....(((....))))))...'
#'..((((((...))).(((...))).(((...))))))'
#'..((((...(((...)))..)))(((....(((...)))...)))...'










































































































































































































































































































































































