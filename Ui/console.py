from Domain.obiect import get_id, format_afisare, get_locatie
from Logic.CRUD import adaugare_obiect, sterge_obiect, modificare_obiect, get_by_id
from Logic.functionalitati import mutare_locatie, concatenare_descriere, cel_mai_mare_pret_per_locatie, \
    ordonare_crescatoare_pret, suma_preturi_per_locatie
from simple_colors import *
import copy


def ui_adauga_obiect(lista):
    undo_lista = copy.deepcopy(lista)
    # id
    try:
        id = int(input("Introduceti id-ul:"))
        for obiect in lista:
            if get_id(obiect) == id:
                raise KeyError("Valoare repetata")
        if id <= 0:
            raise ValueError("Valoare nula id")  # inainte / pasi
    except ValueError:
        print(red("Valoare incorecta. Id-ul trebuie sa fie un numar intreg nenul", ["italic"]))
        return lista, undo_lista
    except KeyError:
        print(red("Id-ul dat apartine deja altui obiect.", ["italic"]))
        return lista, undo_lista
    # nume
    try:
        nume = input("Introduceti numele:")
        if len(nume) == 0:
            raise ValueError("Valoare nula nume")
    except ValueError:
        print(red("Valoare incorecta. Numele trebuie sa fie nenul.", ["italic"]))
        return lista, undo_lista
    # descriere
    try:
        descriere = input("Introduceti descrierea:")
        if len(descriere) == 0:
            raise ValueError("Valoare nula descriere")
    except ValueError:
        print(red("Valoare incorecta. Descrierea trebuie sa fie nenula.", ["italic"]))
        return lista, undo_lista
    # pret
    try:
        pret = float(input("Introduceti pretul:"))
        if pret < 0:
            raise ValueError
        # ValueError prinde si cazul in care se citeste un string in loc de float
    except ValueError:
        print("Pretul trebuie sa fie un numar pozitiv de tip float.")
        return lista, undo_lista
    # locatie
    try:
        locatie = input("Introduceti locatia:")
        if len(locatie) != 4:
            raise ValueError("Lungime incorecta a locatiei")
    except ValueError:
        print(red("Valoare incorecta. Locatia trebuie sa aiba 4 caractere.", ["italic"]))
        return lista, undo_lista
    # returnare lista cu obiectul adaugat
    return adaugare_obiect(lista, id, nume, descriere, pret, locatie), undo_lista


def ui_sterge_obiect(lista):
    undo_lista = copy.deepcopy(lista)
    try:
        id = int(input("Introduceti id-ul obiectului pe are vreti sa il stergeti:\n"))
        if get_by_id(lista, id) is None:
            raise KeyError("Nu exista obiect cu cheia data")
    except KeyError:
        print(red("Nu exista un obiect cu id-ul dat.", ["italic"]))
        return lista, undo_lista
    # returnare lista modificata
    return sterge_obiect(lista, id), undo_lista


def ui_afisare(lista):
    for obiect in lista:
        print(format_afisare(obiect) + "\n")


def ui_modificare(lista):
    undo_lista = copy.deepcopy(lista)
    # id
    try:
        id = int(input("Introduceti id-ul obiectului pe are vreti sa il modificati:\n"))
        if get_by_id(lista, id) is None:
            raise KeyError("Nu exista obiect cu cheia data")
    except KeyError:
        print(red("Nu exista un obiect cu id-ul dat.", ["italic"]))
        return lista, undo_lista
    # nume
    nume = input("Introduceti un nume nou sau nimic pentru a nu schimba:\n")
    # descriere
    descriere = input("Introduceti o descriere noua sau nimic pentru a nu schimba:\n")
    # pret
    pret = float(input("Introduceti un pret nou sau -1 pentru a nu schimba:\n"))
    # locatie
    try:
        locatie = input("Introduceti o locatie noua sau nimic pentru a nu schimba:\n")
        if locatie != "" and len(locatie) != 4:
            raise ValueError("Lungime incorecta a locatiei")
    except ValueError:
        print(red("Valoare incorecta. Locatia trebuie sa aiba 4 caractere.", ["italic"]))
        return lista, undo_lista
    # returnare lista modificata
    return modificare_obiect(lista, id, nume, descriere, pret, locatie), undo_lista


def ui_mutare(lista):
    undo_lista = copy.deepcopy(lista)
    ok = False
    while ok is False:
        ok = True
        try:
            sala_init = input("Introduceti din ce sala vreti sa mutati obiectele.\n")
            if len(sala_init) != 4:
                raise ValueError("Lungime incorecta a locatiei")

        except ValueError:
            print(red("Sala trebuie sa aiba 4 caractere.", ["italic"]))
            ok = False
    ok = False
    while ok is False:
        ok = True
        try:
            sala_fin = input("Introduceti in care sala vreti sa mutati obiectele.\n")
            if len(sala_fin) != 4:
                raise ValueError("Lungime incorecta a locatiei")

        except ValueError:
            print(red("Sala trebuie sa aiba 4 caractere.", ["italic"]))
            ok = False
    return mutare_locatie(lista, sala_init, sala_fin), undo_lista


def ui_concatenare(lista):
    undo_lista = copy.deepcopy(lista)
    pret_citit = int(input("Introduceti un pret.\n"))
    sir = input("Introduceti sirul pe care vreti sa il atasati obiectelor "
                "cu pret mai mare decat valoare data.\n")
    return concatenare_descriere(lista, pret_citit, sir), undo_lista


def printare_lista_pret_locatie(dictionare):
    for d in dictionare:
        locatie = d["locatie"]
        pret = d["pret_maxim"]
        print(f"Locatia {locatie} are pretul maxim {round(pret, 2)}")


def ui_cel_mai_mare_pret_per_locatie(lista):
    print("Lista cu locatiile si preturile lor maxime:")
    printare_lista_pret_locatie(cel_mai_mare_pret_per_locatie(lista))


def ui_ordonare_pret(lista):
    undo_lista = copy.deepcopy(lista)
    return ordonare_crescatoare_pret(lista), undo_lista


def printare_suma_preturi_per_locatie(dictionare):
    for d in dictionare:
        locatie = d["locatie"]
        suma = d["suma_preturi"]
        print(f"Locatia {locatie} are suma preturilor {suma}")


def ui_suma_preturi_per_locatie(lista):
    print("Lista sumelor pentru fiecare locatie:")
    printare_suma_preturi_per_locatie(suma_preturi_per_locatie(lista))


def f_undo_lista(undo_lista):
    try:
        with open("./output.txt", "r") as f:
            lines = f.readlines()
            print(len(lines))
            if len(lines) >= 1:
                last_line = lines[len(lines) - 1]
                if len(lines) > 1:
                    with open("./output.txt", "w") as g:
                        for line in lines:
                            if line.strip("\n") != last_line:
                                g.write(line)
                return last_line
            else:
                raise TypeError("0 operatii ramase")
    except TypeError:
        print(red("Nu mai sunt operatii facute!", ['italic']))
        return undo_lista


def meniu_principal():
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n",
          magenta("\t\tMeniu Principal\n", ['bold']),
          "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
    print("1.C.R.U.D.")
    print("f.Afisare lista")
    print("2.Mutare dintr-o sala in alta")
    print("3.Concatenare un sir la descriere in functie de pret")
    print("4.Afisati cel mai mare pret per fiecare locatie")
    print("5.Ordonare crescatoare lista obiectelor dupa pret")
    print("6.Afisarea sumelor prețurilor pentru fiecare locație")
    print("u.Undo la ultima operatie facuta")
    print("x.Iesire\n")


def meniu_crud():
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n",
          magenta('\t\tC.R.U.D\n', ['bold']),
          "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
    print("a.Adaugare obiect la lista")
    print("s.Stergere obiect din lista")
    print("m.Modificare unui obiect din lista")
    print("x.Inapoi\n")


def run_menu_crud(lista, undo_lista):
    meniu_crud()
    op = input(yellow('Alegeti o optiune:\n', ['bold']))
    if op == "a":
        lista, undo_lista=ui_adauga_obiect(lista)
        return lista, undo_lista, True
    elif op == "s":
        lista, undo_lista=ui_sterge_obiect(lista)
        return lista, undo_lista, True
    elif op == "m":
        lista,undo_lista=ui_modificare(lista)
        return lista, undo_lista, True
    elif op == "x":
        return lista, undo_lista, False
    else:
        print(red("Optiune invalida.", ['bold']))
        return lista, undo_lista, False


def run_menu(lista, undo_lista):
    """f1 = open('./output.txt', 'a', buffering=1)
    f1.write(str(undo_lista))"""
    lists = []
    while True:
        meniu_principal()
        op = input(yellow('Alegeti o optiune:\n', ['bold']))
        if op == "1":
            lista, undo_lista, done = run_menu_crud(lista, undo_lista)
            if done == True:
                lists.append(undo_lista)
        elif op == "f":
            ui_afisare(lista)
        elif op == "2":
            lista, undo_lista = ui_mutare(lista)
            lists.append(undo_lista)
            print(yellow("Obiectele au fost mutate in sala data!", ["italic"]))
        elif op == "3":
            lista, undo_lista = ui_concatenare(lista)
            lists.append(undo_lista)
            print(yellow("Sirul dat a fost concatenat la obiectele cu pret mai mare decat cel dat!", ["italic"]))
        elif op == "4":
            ui_cel_mai_mare_pret_per_locatie(lista)
        elif op == "5":
            lista, undo_lista = ui_ordonare_pret(lista)
            lists.append(undo_lista)
            print(yellow("Obiectele au fost ordonate!", ["italic"]))
        elif op == "6":
            ui_suma_preturi_per_locatie(lista)
        elif op == "u":
            if len(lists) > 0:
                lista = lists[len(lists) - 1]
                lists.pop()
            else:
                print(red("Nu mai sunt operatii facute!"))
            # lista = f_undo_lista(undo_lista)
        elif op == "x":
            # f1.close()
            break
        else:
            print(red("Optiune invalida.", ['bold']))
        """if op == "1" and op == "2" and op == "3" and op == "4" and op == "5":
            #f1.write(str(undo_lista))"""
