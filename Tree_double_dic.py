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

def utworzDrzewo(elementy):
    slownikDoDrzewa = {-1: 'korzen'}
    drzewo = {-1: set([])}
    for ind, e in enumerate(elementy):
        slownikDoDrzewa.update({ind: e})
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
        if ind == 0:
            continue
        else:
            print(s, slownik[ind-1])



d = (utworzDrzewo('ldpdpdsdpdpdl')[0])
seq = dfs(d, -1)

#print(seq)

#print(utworzDrzewo('ldpdpdsdpdpdl')[0])

#print(utworzDrzewo('ldpdpdsdpdpdl')[1])

slownik = (utworzDrzewo('ldpdpdsdpdpdl')[1])
odtworzElementy(seq, slownik)
