#Anna Glinka
#Bioinformatyka sturkturalna

def metrykaHausdorffa(S1, S2):

    mapaS1 = {}

    stos = []
    for i, j in enumerate(S1):
            if j == '(':
                    stos.append(i)
            elif j == ')':
                    para1 = stos.pop()
                    para2 = i
                    mapaS1[para1] = para2
    mapaS2 = {}
    stos = []
    for i, j in enumerate(S2):
            if j == '(':
                    stos.append(i)
            elif j == ')':
                    para1 = stos.pop()
                    para2 = i
                    mapaS2[para1] = para2
                    
    print("mapaS1" , mapaS1)
    print("mapaS2", mapaS2)
  
    wie = len(mapaS1) + 1
    kol = len(mapaS2) + 1
    print("kol:", kol, "wie:", wie)

    Matrix = [[0 for i in range(kol)] for i in range(wie)]
    print(Matrix)
    i = 0
    j = 0   
    for keys,values in mapaS1.items():
        for keys2,values2 in mapaS2.items():
            Matrix[i][j] = max(abs(keys2 - keys), abs(values2 - values))
            j = j + 1
        i = i + 1
        j = 0


    print("po wypelnieniu")
    for i in range(0, wie):
        for j in range(0, kol):
            print( Matrix[i][j], end=" ")
        print("")


    for i in range(0, wie-1):
        minRz = Matrix[i][0]
        for j in range(0, kol-1):
            if Matrix[i][j] < minRz:
                minRz = Matrix[i][j]
            Matrix[i][kol-1] = minRz 
     
    
    for j in range(0, kol-1):
        minKol = Matrix[0][j]
        for i in range(0, wie-1):
            if Matrix[i][j] <  minKol:
                 minKol = Matrix[i][j]
            Matrix[wie-1][j] = minKol
          

    print("po sumowaniu")
    for i in range(0, wie):
        for j in range(0, kol):
            print(Matrix[i][j], end=" ")
        print("")

    MaxPoRzedach =  Matrix[0][kol-1]
    for i in range(1, wie-1):
        if Matrix[i][kol-1] > MaxPoRzedach:
            MaxPoRzedach = Matrix[i][kol-1]
    print("MaxPoRzedach ", MaxPoRzedach)

    MaxPoKolum = Matrix[wie-1][0];
    for j in range(1, kol-1):
        if Matrix[wie-1][j] > MaxPoKolum :
            MaxPoKolum  =  Matrix[wie-1][j];
    print("MaxPoKolum ",   MaxPoKolum )

    return max(MaxPoRzedach,MaxPoKolum);
    

       

    
if __name__ == "__main__":
     import sys
     S1 = ".........((((...))))."
     S2 = "........((((...)))).."
     S3 = ".((((...))))..................."
     S4 = ".((((...))))...........(...)..."
     print("odleglosc sekwencji: ", metrykaHausdorffa(S3, S4))

    

     




    



















