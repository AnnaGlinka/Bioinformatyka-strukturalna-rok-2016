import re


def elementyStruktury(RNA_kropkowo_nawiasowa):
    mapaWiazan = {}
    stos = []
    spinkiDoWlosow = []
    kropki = []
    pojedynczyLancuch = []
    petla = []
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

    #print(mapaWiazan)
    spinka = re.compile('[(][.]{1,500}[)]')
    kropka = re.compile('[.]{1,1000}')


    spinkaIterator = spinka.finditer(RNA_kropkowo_nawiasowa)
    for sp in spinkaIterator:
        spinkiDoWlosow.append(sp.span())
    for sp in spinkiDoWlosow:
        print("spinka", sp)

    kropkiIterator = kropka.finditer(RNA_kropkowo_nawiasowa)
    for kr in kropkiIterator:
        kropki.append(kr.span())
    #for kr in kropki:
        #print("kropki", kr)
    for kr in kropki:
        poczatek = kr[0]
        koniec = kr[1]
        if poczatek == 0 or koniec>len(RNA_kropkowo_nawiasowa)-1:
            pojedynczyLancuch.append((poczatek,koniec-1))
            continue
        if RNA_kropkowo_nawiasowa[poczatek-1]==')' and RNA_kropkowo_nawiasowa[koniec]=='(':
            pojedynczyLancuch.append((poczatek,koniec-1))
            continue
    





if __name__ == "__main__":
 
     #elementyStruktury('..((((...(((...)))..)))(((....(((...)))...)))...')
     #elementyStruktury('..(((...)))..')
     elementyStruktury('....((((((..((((........)))).(((((.......)))))).....(((((.......))))))))))')
     #elementyStruktury('..((((((...)))(((...)))(((...)))))).')
    # elementyStruktury('(((((((((...((((((.........))))))........((((((.......))))))..)))))))))')
    

     

#'((((((....)))....(((....))))))...'
#'..((((((...))).(((...))).(((...))))))'
#'..((((...(((...)))..)))(((....(((...)))...)))...'