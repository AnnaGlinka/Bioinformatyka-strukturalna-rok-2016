#Anna Glinka
#Bioinformatyka sturkturalna

def dfs(graf, start):
    odwiedzone, stos, dfs_tab = set(), [start], []
 
    while stos:
        wierzcholek = stos.pop()
        if wierzcholek not in odwiedzone:
            stos.sort()
            odwiedzone.add(wierzcholek)
            dfs_tab.append(wierzcholek)
            stos.extend(graf[wierzcholek] - odwiedzone)
    return dfs_tab

def utworzDrzewo(elem):

    elementy = ""
    for e in elem:
        if e != 'd':
            elementy += e

    print(elementy)
    slownikDoDrzewa = {-1: ['korzen', 1]}
    drzewo = {-1: set([])}

    ind = 0
   

    while ind < len(elementy):
        print("zewnetrzna", ind, elementy[ind])
       
        '''
        if elementy[ind] == 'x':
             print("e=x")
             for ind2, e in enumerate(elementy[ind:], start=ind):
                print("costam", ind2, e, ind)
                if e =='s':
                    ind = ind2
                    break
         '''

        ind+=1
        

    '''
    for ind, e in enumerate(elementy):
        print("zewnetrzna e=", e, ind)
        if e == 'x':
            print("e=x")
            ind = 9

        
        if e == 'x':
            print('x na indeksie ', ind)
            for ind3, i in enumerate(elementy[0:], start=0):
                print("controla", i, ind3)

            for ind2, e2 in enumerate(elementy[ind:], start=ind):
                print("costam", ind2, e2, ind)
                if e2 =='s':
                    ind +=4
                    continue
        
        slownikDoDrzewa.update({ind: [e, 1]})
        if elementy[ind-1] == 's':
            drzewo.update({ind-1: set([])})
            #return drzewo, slownikDoDrzewa
        
        if ind == 0:
            #print("ind", ind)
            drzewo.update({-1: set([ind])})
        else:
            drzewo.update({ind-1: set([ind])})

    drzewo.update({ind: set([])})
    '''
    return drzewo, slownikDoDrzewa
    

def odtworzElementy(seq, slownik):
    print("seq", seq)
    print("slownik", slownik)
    for ind, s in enumerate(seq):
        print(s, slownik[ind-1])
        '''
        if ind == 0:
            continue
   
        else:
            print(s, slownik[ind-1])

        '''


#d = (utworzDrzewo('ppxppxsxppsppxppxsxppxpspxpspxppxppxsxppxpp')[0]) #drzewo 7
#d = (utworzDrzewo('ppx[ppx[s]x[ppspp]xpp]x[s]x[ppx[psp]x[psp]xpp]x[ppx[s]x[s]xpp]xpp')[0]) #drzewo 7
d = (utworzDrzewo('pp[pp[s][ppspp]pp][s][pp[psp][psp]pp][pp[s][s]pp]pp')[0]) #drzewo 7
'''

print('ldpdpdsdpdpdl')
d = (utworzDrzewo('ldpdpdsdpdpdl')[0])

seq = dfs(d, -1)

print(seq)

print(utworzDrzewo('ldpdpdsdpdpdl')[0])

#print(utworzDrzewo('ldpdpdsdpdpdl')[1])

slownik = (utworzDrzewo('ldpdpdsdpdpdl')[1])
odtworzElementy(seq, slownik)


print("-------------------")
str2 = 'dpdpdxdpdpdsdpdpdxdsdxdpdpd'
print(str2)

d2 = (utworzDrzewo(str2)[0])
print(d2)
slownik2 = (utworzDrzewo(str2)[1])
#seq2 = dfs(d2, -1)

#print(seq2)
#odtworzElementy(seq2, slownik2)
'''


