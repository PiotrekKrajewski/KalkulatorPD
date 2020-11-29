from random import randint


def randomowe_liczby(lista, x=10):
    for x in range(0, x):
        liczba = randint(1, 100)
        if liczba % 2 == 0:
            print(f'Wygenerowana liczba {liczba} jest podzielna przez 2.')
            lista.append(liczba)
    return 'Funkcja randomowe_liczby zakończyła swoje działanie', lista

listaa = []
print(randomowe_liczby(listaa, 25))