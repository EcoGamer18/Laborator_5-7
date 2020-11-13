from Tests.test_functionalitati import test_mutare_locatie, test_concatenare_descriere, \
    test_cel_mai_mare_pret_per_locatie, test_ordonare_crescatoare_pret, test_suma_preturi_per_locatie
from Tests.tests_domain import test_domeniu
from Tests.tests_logic_crud import *


def run_all():
    test_sterge_obiect()
    test_adaugare_obiect()
    test_modificare_obiect()
    test_domeniu()
    test_mutare_locatie()
    test_concatenare_descriere()
    test_cel_mai_mare_pret_per_locatie()
    test_ordonare_crescatoare_pret()
    test_suma_preturi_per_locatie()
