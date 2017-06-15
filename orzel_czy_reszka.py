# Program symuluje 100 rzutów monetą.
import random
liczba_reszek=0
liczba_orlow=0
for i in range(0,100):
    liczba_losowa = random.randrange(0, 2)
    if liczba_losowa == 0:
        liczba_reszek=liczba_reszek+1
    elif liczba_losowa == 1:
        liczba_orlow=liczba_orlow+1
print("Liczba reszek wynosi: ")
print (liczba_reszek)
print("Liczba orlow wynosi: ")
print(liczba_orlow)



