

def utworzDrzewo(elementy):
    print(elementy)
    ind = 0
    wyjscie = ""
    licznikNawiasow = 0
    maxLicznikNawiasow = 0
    licznikX = 1
    while ind < len(elementy):
        #print(elementy[ind], licznikNawiasow)

        if(elementy[ind] == '['):
            wyjscie += 'x'
            #wyjscie += str(licznikX)
            licznikX+=1
            
        else:
            wyjscie +=elementy[ind]

        if elementy[ind] == '[':
            licznikNawiasow +=1
       
        if elementy[ind] == 's':
            
            #wyjscie += 's'
            while elementy[ind] != ']':
                #print("------", elementy[ind], licznikNawiasow)
                if ind >= len(elementy)-1:
                      #print("wyj", wyjscie)
                      return wyjscie
                #print("w while z ]", elementy[ind])
                if elementy[ind] == '[':
                   licznikNawiasow +=1
                if elementy[ind] == ']':
                   licznikNawiasow -=1
                ind += 1
            #print("po while z ]")   
      

        if elementy[ind] == ']':
            licznikNawiasow -=1
            while elementy[ind] != '[':
                #print("<<<<", elementy[ind], licznikNawiasow)
                if ind >= len(elementy)-1:
                      #print("wyj", wyjscie)
                      return wyjscie
                #print("w while z [...", elementy[ind])
                ind += 1
                if elementy[ind] == '[':
                   licznikNawiasow +=1
                if elementy[ind] == ']':
                   licznikNawiasow -=1
               
                
            #print("po while z [...")   

        #print(elementy[ind], ind)
        
        #wyjscie += elementy[ind]
        ind +=1


        #print(wyjscie)
    return wyjscie
      
      


str1 = 'pp[pp[s][ppspp]pp][s][pp[psp][psp]pp][pp[s][s]pp]pp' 
str2 = 'psp'
wyj = ""
print(utworzDrzewo(str1))
print(utworzDrzewo(str2))
#print(d)