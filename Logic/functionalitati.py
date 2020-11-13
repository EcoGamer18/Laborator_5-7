from typing import List

from Domain.obiect import get_locatie, get_id, get_pret, get_descriere
from Logic.CRUD import modificare_obiect


def mutare_locatie(lista_obiecte, sala_init, sala_fin):
    """
    Muta obiectele dintr-o sala in alta

    :param lista_obiecte:
    :param sala_init: sala initiala
    :param sala_fin: sala in care trebuie sa ajunga obiectele
    :return: lista modificata
    """
    for obiect in lista_obiecte:
        if get_locatie(obiect) == sala_init:
            lista_obiecte = modificare_obiect(lista_obiecte, get_id(obiect), "", "", -1, sala_fin)
    return lista_obiecte


def concatenare_descriere(lista_obiecte, pret, sir):
    """
    Concateneaza la descrierea unui obiect un sir dat daca pretul obiectului este mai mare decat pretul dat

    :param lista_obiecte: lista obiectelor
    :param pret: pretul dat
    :param sir: sirul dat
    :return: lista modificata
    """
    for object in lista_obiecte:
        if get_pret(object) > pret:
            object["descriere"] = get_descriere(object) + sir
    return lista_obiecte


def cautare_locatie(dictionar, locatie_cautata):
    """
    Cauta intr-o lista de dictionare de forma
    {"locatie": " string locatie","pret_maxim": nr intreg pret}
    daca o locatie data exista

    :param dictionar: lista de dictionare cu forma de mai sus
    :param locatie_cautata: locatia cautata in dictionare
    :return: True/False daca locatie exista/nu exista
    """
    for d in dictionar:
        if d["locatie"] == locatie_cautata:
            return True
    return False


def pret_locatie(dictionar, locatie_cautata):
    """
    Returneaza pretul maxim de la o locatie data

    :param dictionar: lista de dictionare
    :param locatie_cautata: locatia la care se cauta pretul maxim
    :return: pretul maxim cautat
    """
    for d in dictionar:
        if d["locatie"] == locatie_cautata:
            return d["pret_maxim"]


def cel_mai_mare_pret_per_locatie(lista_obiecte):
    """
    Returneaza o lista de dictionare care contin locatia si pretul maxim de la acea locatie

    :param lista_obiecte: lista de obiecte
    :return: lista de dictionare de forma de mai sus
    """
    dictionar = []
    for obiect in lista_obiecte:
        if cautare_locatie(dictionar, get_locatie(obiect)) == False:
            dictionar.append({"locatie": get_locatie(obiect), "pret_maxim": get_pret(obiect)})
        else:
            if pret_locatie(dictionar, get_locatie(obiect)) < get_pret(obiect):
                for d in dictionar:
                    if d["locatie"] == get_locatie(obiect):
                        d["pret_maxim"] = get_pret(obiect)
    return dictionar


def ordonare_crescatoare_pret(lista_obiecte):
    """
    Ordoneaza crescator lista de obiecte in functie de pret

    :param lista_obiecte: lista de obiecte
    :return: lista de obiecte ordonata
    """
    lista_modificata = sorted(lista_obiecte, key=lambda d: d["pret"])
    return lista_modificata


def suma_pret_locatie(dictionar, locatie_cautata):
    """
    Returneaza suma preturilor de la o locatie data

    :param dictionar: lista de dictionare cu locatia si suma preturilor obiectelor de la locatie
    :param locatie_cautata: locatia data
    :return: suma preturilor in locatia respectiva
    """
    for d in dictionar:
        if d["locatie"] == locatie_cautata:
            return d["suma_preturi"]


def suma_preturi_per_locatie(lista_obiecte):
    """
    Returneaza o lista cu dictionare de forma locatie si suma preturilor obiectelor de la locatie

    :param lista_obiecte: lista obiectelor
    :return: lista de dictionare cu sumele cerute
    """
    dictionar = []
    for obiect in lista_obiecte:
        if cautare_locatie(dictionar, get_locatie(obiect)) == False:
            dictionar.append({"locatie": get_locatie(obiect), "suma_preturi": get_pret(obiect)})
        else:
            for d in dictionar:
                if d['locatie'] == get_locatie(obiect):
                    d["suma_preturi"] += get_pret(obiect)
    for d in dictionar:
        d["suma_preturi"] = round(d["suma_preturi"], 2)
    return dictionar
