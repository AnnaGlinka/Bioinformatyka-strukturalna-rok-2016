
import numpy as np
punktacja = {'dopasowanie':1, 'niedopasowanie':-1, 'przerwa':-1}

def sprawdzDopasowanie(x, y):
    if x == y:
        return punktacja['dopasowanie']
    elif x == '-' or y == '-':
        return punktacja['przerwa']
    else:
        return punktacja['niedopasowanie']

def NeedlemanWunsch(seq1, seq2):
    m, n = len(seq1), len(seq2)
    punkty = np.zeros((m+1, n+1))  
 # Faza inicjalizacji macierzy---------------------------------------------------------
    for i in range(m+1):
        punkty[i][0] = punktacja['przerwa'] * i
    for j in range(n+1):
        punkty[0][j] = punktacja['przerwa'] * j
 # Wypelnienie macierzy punktacji-------------------------------------------------------
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            przek = punkty[i-1][j-1] + sprawdzDopasowanie(seq1[i-1], seq2[j-1])
            D = punkty[i-1][j] + punktacja['przerwa']
            I = punkty[i][j-1] + punktacja['przerwa']
            punkty[i][j] = max(przek, D, I)
    i = m
    j = n
    dopasowanie_1 = "" 
    dopasowanie_2 = ""
 # Przejscie przez macierz-----------------------------------------------------------
    while (i>0 and j>0):
        punkty_teraz = punkty[i][j]
        punkty_przek = punkty[i-1][j-1]
        punkty_L = punkty[i][j-1]
        punkty_gora = punkty[i-1][j]
       
        if punkty_teraz == punkty_przek + sprawdzDopasowanie(seq1[i-1], seq2[j-1]):
            dop_1 = seq1[i-1]
            dop_2 = seq2[j-1]
            i = i-1
            j = j-1
        elif punkty_teraz == punkty_gora + punktacja['przerwa']:
            dop_1 = seq1[i-1]
            dop_2 = "-"
            i -= 1
        elif punkty_teraz == punkty_L + punktacja['przerwa']:
            dop_1 = "-"
            dop_2 = seq2[j-1]
            j -= 1
        dopasowanie_1+=dop_1
        dopasowanie_2+=dop_2
            
    while i>0:
        dop_1 = seq1[i-1]
        dop_2 = "-"
        dopasowanie_1+=dop_1
        dopasowanie_2+=dop_2
        i -= 1
    while j>0:
        dop_1 = "-"
        dop_2 = seq2[j-1]
        dopasowanie_1+=dop_1
        dopasowanie_2+=dop_2
        j -= 1
    
    dopasowanie_1 = dopasowanie_1[::-1]
    dopasowanie_2 = dopasowanie_2[::-1]
    sekwencja = len(dopasowanie_1)
    punktacjaSekwencji = 0
    identycznosc = 0
    for i in range(sekwencja):
        dop_1 = dopasowanie_1[i]
        dop_2 = dopasowanie_2[i]
        if dop_1 == dop_2:
            identycznosc += 1
            punktacjaSekwencji += sprawdzDopasowanie(dop_1, dop_2)
        else: 
            punktacjaSekwencji += sprawdzDopasowanie(dop_1, dop_2)
        
    identycznosc = identycznosc/sekwencja * 100
    print("Po dopasowaniu")
    print("sekwencja 1:",dopasowanie_1)
    print("sekwencja 2:",dopasowanie_2)
    print("Procent identycznosci: %2.1f" % identycznosc)
    print("Punktacja:", punktacjaSekwencji)
    print()
   


NeedlemanWunsch("12010","1220010")
NeedlemanWunsch("12101110","1211010")
NeedlemanWunsch("11151120011200112101001112121120000","11141120011210101011121100")
