"""
Lab 5
B.Scrieți un program pentru gestionarea unui inventar  dintr-o instituție.
Vor  fi  suportate operațiile:
1.Adăugare / ștergere / modificare obiect:
se efectuează pe bază de număr de inventar/ ID.
Un obiect conține: ID, nume, descriere (nenule), preț achiziție,
locație (4 caractere).

Lab 6
2.Mutarea tuturor obiectelor dintr-o sală în alta.
3.Concatenarea unui string citit la toate descrierile obiectelor
cu prețul mai mare decât o valoare citită.


"""
import copy
from Logic.CRUD import adaugare_obiect
from Tests.run_all import run_all
from Ui.console import run_menu


def main():
    lista = []
    lista = adaugare_obiect(lista, 1, "Obiect intai", "Descriere", 150.0, "P1S8")
    lista = adaugare_obiect(lista, 2, "Obiect doi", "Descccriiiiere", 2005.9, "P2S1")
    lista = adaugare_obiect(lista, 3, "Obiect trei", "O forma geometrica", 20.8, "SiMP")
    lista = adaugare_obiect(lista, 4, "Obiect patru", "O forma analitica", 205.8, "SiMP")
    undo_lista = copy.deepcopy(lista)
    run_menu(lista,undo_lista)


run_all()
main()
