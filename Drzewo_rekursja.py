

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
    print(elementy)

    kolejka = []
    licznikNawiasow = 0
    slownikDoDrzewa = {-1: ['korzen', 1]}
    drzewo = {-1: set([])}

    ind = 0
   
    #------------------------------------------------------------------
    while ind < len(elementy):
        #print("zewnetrzna", ind, elementy[ind])
        st = ""

        if elementy[ind] =='[':
            licznikNawiasow+=1
            ind +=1
            drzewo.update({ind-1: set([ind])})
            if elementy[ind] == 'p' or elementy[ind] == 'w':
                slownikDoDrzewa.update({ind: [elementy[ind], 1]})
            elif elementy[ind] == 's':
                slownikDoDrzewa.update({ind: [elementy[ind], 0]})
            else:
                slownikDoDrzewa.update({ind: [elementy[ind], 3]})
           
            
            while licznikNawiasow != 0:
                #print("wewnatrz", elementy[ind], licznikNawiasow)
                if elementy[ind] =='[':
                   licznikNawiasow+=1
                   #print("otwieram")
      
                elif elementy[ind] ==']':
                   licznikNawiasow-=1
                   #print("zamykam")
                else: 
                    print(elementy[ind], ind)
                    st += elementy[ind]
                ind +=1
            print("++++++++++++", st) 
            kolejka.append(st)

        if ind == 0:
            #print("ind", ind)
            drzewo.update({-1: set([ind])})
        else:
            drzewo.update({ind-1: set([ind])})


        if elementy[ind] == 'p' or elementy[ind] == 'w':
            slownikDoDrzewa.update({ind: [elementy[ind], 1]})
        elif elementy[ind] == 's':
           slownikDoDrzewa.update({ind: [elementy[ind], 0]})
        else:
            slownikDoDrzewa.update({ind: [elementy[ind], 3]})
         
     
       
        drzewo.update({ind: set([])})
        ind+=1

        print("kolejka", kolejka)
        #----------------------------------------------
    
    print(slownikDoDrzewa)
    print("---------------------------------") 
    print("drzewo",drzewo)
    print("---------------------------------") 

    return drzewo















#str = 'pp[pp[s][ppspp]pp][s][pp[psp][psp]pp][pp[s][s]pp]pp' #dla drzewa 7
str = 'ppx[ppx[s]x[ppspp]xpp]x[s]x[ppx[psp]x[psp]xpp]x[ppx[s]x[s]xpp]xpp'
d = utworzDrzewo(str)

seq = dfs(d, -1)
print(seq)