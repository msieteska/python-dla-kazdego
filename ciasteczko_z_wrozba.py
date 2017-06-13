# Program symuluje ciasteczko z wróżbą
import random

liczba_losowa=random.randrange(0,5)
if liczba_losowa==0:
    print("Będziesz szczęśliwy")
elif liczba_losowa==1:
    print("Będziesz bogaty")
elif liczba_losowa==2:
    print("Spełni się Twoje marzenie")
elif liczba_losowa==3:
    print("Wyjdziesz młodo za mąż")
else:
    print ("Umrzesz młodo")

