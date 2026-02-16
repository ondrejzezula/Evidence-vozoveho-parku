import sqlite3

DB_NAME = "vozidla.db"


def get_connection():
    """Vrátí připojení k databázi."""
    return sqlite3.connect(DB_NAME)


# ==========================================
# CELKOVÉ NÁKLADY VŠECH VOZIDEL
# ==========================================
def spocitej_celkem():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(cena)
        FROM servisy
    """)

    result = cursor.fetchone()[0]
    conn.close()

    return result if result else 0


# ==========================================
# NÁKLADY PRO KONKRÉTNÍ VOZIDLO
# ==========================================
def spocitej_pro_vozidlo(vozidlo_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(cena)
        FROM servisy
        WHERE vozidlo_id = ?
    """, (vozidlo_id,))

    result = cursor.fetchone()[0]
    conn.close()

    return result if result else 0


# ==========================================
# NÁKLADY ZA OBDOBÍ
# ==========================================
def spocitej_za_obdobi(datum_od, datum_do):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(cena)
        FROM servisy
        WHERE datum BETWEEN ? AND ?
    """, (datum_od, datum_do))

    result = cursor.fetchone()[0]
    conn.close()

    return result if result else 0


# ==========================================
# PRŮMĚRNÉ NÁKLADY NA JEDEN SERVIS
# ==========================================
def prumerna_cena_servisu():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(cena)
        FROM servisy
    """)

    result = cursor.fetchone()[0]
    conn.close()

    return round(result, 2) if result else 0
