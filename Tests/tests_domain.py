from Domain.obiect import *


def test_domeniu():
    obj = creare_obiect(1, "Masa", "Rosie", 500, "Simm")

    assert get_id(obj) == 1
    assert get_nume(obj) == "Masa"
    assert get_descriere(obj) == "Rosie"
    assert get_pret(obj) == 500
    assert get_locatie(obj) == "Simm"
