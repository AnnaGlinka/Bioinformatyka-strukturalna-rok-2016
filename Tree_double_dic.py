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
    for ind, e in enumerate(elementy):
        #print("e=", e)
        if e == 'x':
            print('x na indeksie ', ind)
            for ind, e in enumerate(elementy):
                print("costam", ind, e)



        slownikDoDrzewa.update({ind: [e, 1]})
        
        
        if elementy[ind-1] == 's':
            drzewo.update({ind-1: set([])})
            return drzewo, slownikDoDrzewa
        
        if ind == 0:
            #print("ind", ind)
            drzewo.update({-1: set([ind])})
        else:
            drzewo.update({ind-1: set([ind])})

    drzewo.update({ind: set([])})


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



print('ldpdpdsdpdpdl')
d = (utworzDrzewo('ldpdpdsdpdpdl')[0])
seq = dfs(d, -1)

print(seq)

print(utworzDrzewo('ldpdpdsdpdpdl')[0])

#print(utworzDrzewo('ldpdpdsdpdpdl')[1])

slownik = (utworzDrzewo('ldpdpdsdpdpdl')[1])
odtworzElementy(seq, slownik)


print("-------------------")
str2 = 'dxdsdxdsdxd'
print(str2)

d2 = (utworzDrzewo(str2)[0])
#slownik2 = (utworzDrzewo(str2)[1])
#seq2 = dfs(d2, -1)

#print(seq2)
#odtworzElementy(seq2, slownik2)
