import datetime


def validate_vehicle(spz, znacka, rok):
    if not spz or not znacka or not rok:
        return False, "Všechna pole musí být vyplněna."

    if not rok.isdigit():
        return False, "Rok musí být číslo."

    year = int(rok)
    current_year = datetime.datetime.now().year

    if year < 1900 or year > current_year:
        return False, "Rok výroby není platný."

    return True, ""

# ===== SERVISY =====

def validate_service(datum, popis, cena):
    if not datum or not popis or not cena:
        return False, "Všechna pole musí být vyplněna."

    try:
        float(cena)
    except ValueError:
        return False, "Cena musí být číslo."

    return True, ""