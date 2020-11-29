from random import randint

class Ksiazka:
    def __init__(self, tytul=None, autor=None, gatunek=None, cena=0.0):
        self.tytul = tytul
        self.autor = autor
        self.gatunek = gatunek
        self.cena = cena

    def __str__(self):
        return 'Tytuł: {s.tytul} | Autor: {s.autor} | Gatunek: {s.gatunek} | Cena: {s.cena}'.format(s=self)

    def zmien_cene_ksiazki(self, nowa_cena=0):
        """Funkcja pozwalająca zmienić cenę książki"""
        if nowa_cena <= 0:
            raise bledna_Cena

        print(f'Aktualna cena książki: {self.tytul}, to: {self.cena}')
        self.cena = nowa_cena
        print(f'Nowa cena książki: {self.tytul}, to: {self.cena}')

    def losowa_ksiazka(lista):
        liczba = randint(0, 4)

        return 'Wylosowana książka to: ', lista[liczba]


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class bledna_Cena(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    pass


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
