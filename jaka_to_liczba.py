# Program symuluje grę w której gracz musi odgadnąć liczbę w okreslonej ilości prób.
print("Mam na myśli pewną liczbę: ")
print("Spróbuj zgadnąć... ale masz tylko 3 próby!")
import random
liczba_wylosowana=random.randrange(0,3)
for i in range(3):
    liczba=int(input("Twoja liczba: "))
    if liczba <liczba_wylosowana:
        print("Za mała!")
    elif liczba>liczba_wylosowana:
        print("Za duża!")
    else:
        print("To ta liczba!")
        break
if liczba_wylosowana != liczba:
    print("Niestety nie udało się!")
print("Miałem na myśli liczbę:", liczba_wylosowana)
