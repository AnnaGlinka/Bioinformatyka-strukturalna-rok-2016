'''

def utworzDrzewo(elementy, wyj):
        if len(wyj)<=1:
            print(wyj)
            return wyj

        print(elementy)
        print("wyj", wyj)

        #licznikNawiasow = 0
      

        while ind < len(elementy):
            print(elementy[ind], ind)

           
            if elementy[ind] =='[':
                print("mam [")
                wyj += 'x'
                utworzDrzewo(ind+1, elementy, wyj)

            
           
           

            wyj += elementy[ind]
            ind +=1
       

        #----------------------------------------------

'''

def utworzDrzewo(elementy):
    print(elementy)
    ind = 0
    wyjscie = ""
    licznikNawiasow = 0
    maxLicznikNawiasow = 0
    while ind < len(elementy):
       
        if elementy[ind] == 's':
            
            wyjscie += 's'
            while elementy[ind] != ']':
                if ind >= len(elementy)-1:
                      print("wyj", wyjscie)
                      return wyjscie
                print("w while z ]", elementy[ind])
                ind += 1
            print("po while z ]")   

        if elementy[ind] == ']':
            licznikNawiasow -=1
           
            while elementy[ind] != '[':
                if ind >= len(elementy)-1:
                      print("wyj", wyjscie)
                      return wyjscie
                print("w while z [...", elementy[ind])
                if elementy[ind] != ']':
                    licznikNawiasow -=1
                ind += 1
            print("po while z [...")   

        #print(elementy[ind], ind)
        wyjscie += elementy[ind]
        ind +=1


        #print(wyjscie)
    return wyjscie
      
      


str = 'pp[pp[s][ppspp]pp][s][pp[psp][psp]pp][pp[s][s]pp]pp' 
str2 = 'psp'
wyj = ""
d = utworzDrzewo(str)
utworzDrzewo(str2)
#print(d)