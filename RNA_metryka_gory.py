#Anna Glinka
#Bioinformatyka sturkturalna

def metrykaGory(S1, S2):
    vS1 = []
    vS2 = []
    S1c = 0
    S2c = 0

    for j in S1:
            if j == '(': 
                S1c+=1
                vS1.append(S1c)
            elif j == ')':
                S1c-=1
                vS1.append(S1c)
            else:
                vS1.append(S1c)

    for j in S2:
            if j == '(': 
                S2c+=1
                vS2.append(S2c)
            elif j == ')':
                S2c-=1
                vS2.append(S2c)
            else:
                vS2.append(S2c)

    return abs(sum(vS1)-sum(vS2))
                   
    
if __name__ == "__main__":
     import sys
     S1 = "..(((.....))).."
     S2 = ".((((.....))))."
     S3 = "..((((...)))).."
   
     print("odleglosc sekwencji: ", metrykaGory(S1, S3))

    

     




    



















