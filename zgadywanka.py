import random
print("Witaj w zgadywance, została wyloswana liczba od 1 - 10")
los = random.randrange(1,11)
for i in range(1,5):
    strzał = int(input('Podaj twój strzał: '))
    if strzał < los and strzał:
        print("Szukana liczba jest większa od podanej!")
    elif strzał > los and strzał:
        print("Szukana liczba jest mniejsza od podanej!")
    elif strzał == los:
        str(i)
        str(los)
        print("Gratuluje! To było",los,"Zgadłeś za",i,"próbą")
    