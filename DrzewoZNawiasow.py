
def ZbudujDrzewo(elem):
    print("wejscie: ", elem)
    i = 0
    wyjscie = []   
    stos = []
    stosGalezi = []
    licznikNawiasow = 0 #zlicza ile razy stos nawiasow stal sie pusty
    galaz = ""
    #-------------------------------------------------------------
    print(elem[0], elem[-1])
    if (elem[0] == 'l' or elem[-1] == 'l'):
        wyjscie.append(1)

    while i < len(elem):
        
        if (elem[i] == 'p' or elem[i] == 'w' or elem[i] == 'z'):
                wyjscie.append(1)
                #print("dodaje 1")
        if (elem[i] == 's' or elem[i] =='r'):
            wyjscie.append(0)
            #print("dodaje 0")
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
                        stosGalezi.append(galaz[1:-1])
                    galaz = ""
                i+=1

        print("stosGalezi", stosGalezi)


        if len(stosGalezi):
           licznikStosu = len(stosGalezi)
           wyjscie.append(licznikStosu)

        while stosGalezi:
            e = stosGalezi.pop()
            print("e=========================", e)
            ind = 0
            licznikNawiasow = 0
            licznikStosu2 = 0
            
            while ind < len(e):
               if (e[ind] == 'p' or e[ind] == 'w' or e[ind] == 'z'):
                   wyjscie.append(1)
               if (e[ind] == 's' or e[ind] =='r'):
                  wyjscie.append(0)
                  #print("dodaje 0")
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
            #print("licznik stosu", licznikStosu)
            #print("licznik stosu2", licznikStosu2)
            if licznikStosu2 != 0:
                wyjscie.append(licznikStosu2)
                #print("dodaje ", licznikStosu2)
            

        i +=1


        #print(wyjscie)
    return wyjscie
      
str1 = 'ppppp[pp[s][ppspp]pp][s][pp[psp][psp]pp][pp[s][s]pp]ppppp' 
str2 = 'ppspp'
str3 = 'l[psp][ppspp]'
str4 = 'pz[pzp[s][ppspp]pwp][s][pp[psp][psp]pp][pp[s][s]pp]wp'
str5 = 'pz[pzp[s][p[s][pp[s][s]pp]p]pwp][s][pp[psp][psp]pp][pp[s][s]pp][pp[s][s]pp]wp'
str6 = 'pz[pzp[s][ppspp]pwp][zsw][pp[psp][psp]pp][pp[s][s]pp]wpl'
str7 = 'lpz[pzp[s][p[s][pp[s][s]pp]p]pwp][s][pp[psp][psp]pp][pp[s][s]pp][pp[s][s]pp]wpl'
#PDB_00547 
str8 = 'l[psp][ppspp]'
#PDB_00142
str9 = 'psp'   
# CRW_00552
str10 = 'l[zpzswpw][psp]l'
#print("wyjscie: ", ZbudujDrzewo(str1))
#print("wyjscie: ", ZbudujDrzewo(str2))
#print("wyjscie: ", ZbudujDrzewo(str3))
#print("wyjscie: ", ZbudujDrzewo(str4))
#print("wyjscie: ", ZbudujDrzewo(str5))
#print("wyjscie: ", ZbudujDrzewo(str6))
print("wyjscie: ", ZbudujDrzewo(str7))
print("wyjscie: ", ZbudujDrzewo(str8))
print("wyjscie: ", ZbudujDrzewo(str9))
print("wyjscie: ", ZbudujDrzewo(str10))



