# Program odgaduje liczbę którą podaje użytkownik.
# Do odgadnięcia liczby zastosowano algotytm "dziel i rządź" ("divide and conquer')
liczba_wybrana = int(input("Wybrana liczba: "))
koniec = 100
poczatek = 0
czy_zgadlem = False
while czy_zgadlem == False:
    proba = int(poczatek + (koniec - poczatek) * 0.5)
    print(proba, poczatek, koniec)
    if liczba_wybrana == proba:
        czy_zgadlem = True
    elif liczba_wybrana < proba:
        koniec = proba
    else:
        poczatek = proba
print("Udało się komputerku! Zgadłeś!")
