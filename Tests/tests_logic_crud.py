from Logic.CRUD import *


def test_adaugare_obiect():
    lista = []
    lista = adaugare_obiect(lista, 1, "Nume frumix", "Cel mai frumix", 156, "SIM9")

    assert get_id(lista[0]) == 1
    assert get_nume(lista[0]) == "Nume frumix"
    assert get_descriere(lista[0]) == "Cel mai frumix"
    assert get_pret(lista[0]) == 156
    assert get_locatie(lista[0]) == "SIM9"


def test_sterge_obiect():
    obj1 = creare_obiect(1, "Numix", "Patrat", 45, "8008")
    obj2 = creare_obiect(2, "Carte", "Paralelipiped", 85, "SIMP")

    lista_obiecte = [obj1, obj2]
    lista_obiecte = sterge_obiect(lista_obiecte, 1)

    assert len(lista_obiecte) == 1
    assert get_by_id(lista_obiecte, 2) == obj2
    assert get_by_id(lista_obiecte, 1) is None

def test_modificare_obiect():
    obj1 = creare_obiect(1, "Numix", "Patrat", 45, "8008")
    obj2 = creare_obiect(2, "Carte", "Paralelipiped", 85, "SIMP")

    lista_obiecte = [obj1, obj2]
    lista_obiecte = modificare_obiect(lista_obiecte,1,"Manual","",100,"")

    obj_update=get_by_id(lista_obiecte,1)
    assert get_nume(obj_update) == "Manual"
    assert get_descriere(obj_update) == "Patrat"
    assert get_pret(obj_update) == 100
    assert get_locatie(obj_update) == "8008"
