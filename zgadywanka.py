import random
print("Witaj w zgadywance, została wyloswana liczba od 1 - 10, masz 4 szanse na zgadniecie co to za liczba(Wpsuj tylko liczby!)")
input("Gotowy?")
los = random.randrange(1,11)
for i in range(1,5):
    strzał = int(input('Podaj twój strzał: '))
    if strzał < los and strzał in range(0,11):
        print("Szukana liczba jest większa od podanej!")
    elif strzał > los and strzał in range(0,11):
        print("Szukana liczba jest mniejsza od podanej!")
    elif strzał == los:
        str(i)
        str(los)
        print("Gratuluje! To było",los,"Zgadłeś za",i,"próbą")
        exit()
    else:
        print("Miales podac liczbe od 1 - 10 -próba :) ")
print("Niestety nie zdgadles :(")
    