def creare_obiect(id, nume, descriere, pret, locatie):
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "locatie": locatie
    }


def get_id(obiect):
    return obiect['id']


def get_nume(obiect):
    return obiect['nume']


def get_descriere(obiect):
    return obiect['descriere']


def get_pret(obiect):
    return obiect['pret']


def get_locatie(obiect):
    return obiect['locatie']


def format_afisare(obiect):
    return f"id: {get_id(obiect)} \nnume: {get_nume(obiect)} \n" \
           f"descriere: {get_descriere(obiect)} \n" \
           f"pret: {get_pret(obiect)}\n" \
           f"locatie: {get_locatie(obiect)}"
