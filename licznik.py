# Program liczy za użytkownika
# Do programu można wprowadzić dowolną liczbę początkową, końcową i odstęp między liczbami
liczba_poczatkowa=int(input("Liczba poczatkowa to: "))
liczba_koncowa=int(input("Liczba końcowa to: "))
odstep=int(input("Odstęp między liczbami to: "))
for i in range (liczba_poczatkowa,liczba_koncowa,odstep):
    print(i, end=" ")
for i in range (liczba_poczatkowa,liczba_koncowa,-odstep):
    print(i,end=" ")
