#Anna Glinka
#Bioinformatyka sturkturalna
def drzewoDFS(elem):
    print("wejscie: ", elem)
  
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
      
str1 = 'lprpl' 
str2 = 'zprpw'
str3 = 'l[s][[s]][s]l'
#PDB_00176
str4 = 'l[psp][[psp]][[psp]][psp]'

str6 = 'lpz[pzp[s][p[s][pp[s][s]pp]p]pwp][[s]][[pp[psp][psp]pp]][[pp[s][s]pp]][pp[s][s]pp]wpl'
str7 = 'pz[pzp[s][ppspp]pwp][[zsw]][[pp[psp][psp]pp]][pp[s][s]pp]wpl'
#PDB_00547 
str8 = 'l[psp][ppspp]'
#PDB_00142
str9 = 'psp'   
# CRW_00552
str10 = 'l[zpzswpw][psp]l'

#PDB_00547 
str11 = 'l[psp][ppspp]'

str12 = ' l[s][wws]l'

print("dfs: ", drzewoDFS(str1))
print("dfs: ", drzewoDFS(str2))
print("dfs: ", drzewoDFS(str3))

#PDB_00176
print("dfs: ", drzewoDFS(str4))

#sek12
print("dfs: ", drzewoDFS(str6))
#sek 11
print("dfs: ", drzewoDFS(str7))
print("wyjscie: ", drzewoDFS(str8))
#PDB_00142
print("dfs: ", drzewoDFS(str9))

# CRW_00552
print("dfs: ", drzewoDFS(str10))
#PDB_00547 
print("dfs: ", drzewoDFS(str11))
#RFA_00642
print("dfs: ", drzewoDFS(str12))




