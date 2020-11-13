from Domain.obiect import get_locatie, get_descriere, get_id
from Logic.CRUD import adaugare_obiect, get_by_id
from Logic.functionalitati import mutare_locatie, concatenare_descriere, cel_mai_mare_pret_per_locatie, pret_locatie, \
    cautare_locatie, ordonare_crescatoare_pret, suma_preturi_per_locatie, suma_pret_locatie


def lista_teste():
    lista = []
    lista = adaugare_obiect(lista, 2, "Obiect doi", "Descccriiiiere", 2005.9, "P2S1")
    lista = adaugare_obiect(lista, 3, "Obiect trei", "Carte despre maate", 20.8, "SiMP")
    lista = adaugare_obiect(lista, 4, "Obiect patru", "Carte despre info", 205.8, "SiMP")
    lista = adaugare_obiect(lista, 5, "Obiect patru", "Carte cu retete", 5.89, "P851")
    lista = adaugare_obiect(lista, 6, "Obiect patru", "Carte despre Minecraft", 50.5, "P851")
    return lista


def test_mutare_locatie():
    lista = lista_teste()
    lista = mutare_locatie(lista, "SiMP", "P5S2")

    assert get_locatie(get_by_id(lista, 3)) == "P5S2"
    assert get_locatie(get_by_id(lista, 4)) == "P5S2"
    assert get_locatie(get_by_id(lista, 2)) == "P2S1"
    assert get_locatie(get_by_id(lista, 5)) == "P851"
    assert get_locatie(get_by_id(lista, 6)) == "P851"


def test_concatenare_descriere():
    lista = lista_teste()
    lista = concatenare_descriere(lista, 51, " Yep Yep")

    assert get_descriere(get_by_id(lista, 2)) == "Descccriiiiere Yep Yep"
    assert get_descriere(get_by_id(lista, 4)) == "Carte despre info Yep Yep"
    assert get_descriere(get_by_id(lista, 3)) == "Carte despre maate"
    assert get_descriere(get_by_id(lista, 6)) == "Carte despre Minecraft"


def test_cel_mai_mare_pret_per_locatie():
    lista = lista_teste()
    dictionar = cel_mai_mare_pret_per_locatie(lista)

    assert dictionar == [{"locatie": "P2S1", "pret_maxim": 2005.9},
                         {"locatie": "SiMP", "pret_maxim": 205.8},
                         {"locatie": "P851", "pret_maxim": 50.5}]
    # get pret maxim la o locatie data
    assert pret_locatie(dictionar, "P2S1") == 2005.9
    assert pret_locatie(dictionar, "SiMP") == 205.8
    assert pret_locatie(dictionar, "P851") == 50.5
    # verificare daca exista locatie
    assert cautare_locatie(dictionar, "SSSS") is False
    assert cautare_locatie(dictionar, "Simp") is False
    assert cautare_locatie(dictionar, "SiMP") is True
    assert cautare_locatie(dictionar, "P2S1") is True


def test_ordonare_crescatoare_pret():
    lista = lista_teste()
    lista = ordonare_crescatoare_pret(lista)

    assert get_id(lista[0]) == 5
    assert get_id(lista[1]) == 3
    assert get_id(lista[2]) == 6
    assert get_id(lista[3]) == 4
    assert get_id(lista[4]) == 2


def test_suma_preturi_per_locatie():
    lista = lista_teste()
    dictionar = suma_preturi_per_locatie(lista)

    assert dictionar == [{"locatie": "P2S1", 'suma_preturi': 2005.9},
                         {"locatie": "SiMP", 'suma_preturi': 226.6},
                         {"locatie": "P851", 'suma_preturi': 56.39}]
    # get suma preturi locatie
    assert suma_pret_locatie(dictionar, "P2S1") == 2005.9
    assert suma_pret_locatie(dictionar, "SiMP") == 226.6
    assert suma_pret_locatie(dictionar, "P851") == 56.39
