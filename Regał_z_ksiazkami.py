from Ksiazka import Ksiazka, bledna_Cena

if __name__ == '__main__':
    ksiazka1 = Ksiazka('Wiedźmin: Ostatnie życzenie', 'Andrzej Sapkowski', 'Fantastyka', 35.99)
    ksiazka2 = Ksiazka('Gambit królowej', 'Tevis Walter', 'Literatura piękna obca', 33.49)
    ksiazka3 = Ksiazka('Rafał Pacześ', 'Grube wióry', 'Literatura piękna polska', 25.95)
    ksiazka4 = Ksiazka('Hannibal: Milczenie Owiec', 'Harris Thomas', 'Thriller', 35.49)
    ksiazka5 = Ksiazka('Hobbit', 'John Ronald Reuel Tolkien', 'Fantastyka', 28.95)

    # print(ksiazka1)
    # print(ksiazka2)
    # print(ksiazka3)
    # print(ksiazka4)
    # print(ksiazka5)

    lista = []
    lista.append(ksiazka1)
    lista.append(ksiazka2)
    lista.append(ksiazka3)
    lista.append(ksiazka4)
    lista.append(ksiazka5)

    for i in range(0, 5, 1):
        print(lista[i])

    try:
        ksiazka1.zmien_cene_ksiazki(20.99)
    except bledna_Cena:
        print('Podałeś wartość mniejszą bądź równą 0.')

    try:
        ksiazka2.zmien_cene_ksiazki(20.00)
    except bledna_Cena:
        print('Podałeś wartość mniejszą bądź równą 0.')

    print(Ksiazka.losowa_ksiazka(lista))
