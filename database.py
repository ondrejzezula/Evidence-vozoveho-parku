import sqlite3
import os

DB_PATH = os.path.join("data", "vozidla.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vozidla (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            spz TEXT NOT NULL UNIQUE,
            znacka TEXT NOT NULL,
            rok INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servisy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vozidlo_id INTEGER NOT NULL,
            datum TEXT NOT NULL,
            popis TEXT NOT NULL,
            cena REAL NOT NULL,
            FOREIGN KEY (vozidlo_id) REFERENCES vozidla(id)
        )
    """)

    conn.commit()
    conn.close()


# ===== VOZIDLA =====

def add_vehicle(spz, znacka, rok):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO vozidla (spz, znacka, rok) VALUES (?, ?, ?)",
        (spz, znacka, rok)
    )
    conn.commit()
    conn.close()


def get_vehicles():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vozidla")
    rows = cursor.fetchall()
    conn.close()
    return rows


# ===== SERVISY =====

def add_service(vozidlo_id, datum, popis, cena):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO servisy (vozidlo_id, datum, popis, cena) VALUES (?, ?, ?, ?)",
        (vozidlo_id, datum, popis, cena)
    )
    conn.commit()
    conn.close()


def get_services_by_vehicle(vozidlo_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, datum, popis, cena FROM servisy WHERE vozidlo_id = ? ORDER BY datum",
        (vozidlo_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

# =====  MAZÁNÍ VOZIDLA =====

def delete_vehicle(vozidlo_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM servisy WHERE vozidlo_id = ?",
        (vozidlo_id,)
    )

    cursor.execute(
        "DELETE FROM vozidla WHERE id = ?",
        (vozidlo_id,)
    )

    conn.commit()
    conn.close()


# =====  MAZÁNÍ SERVISU =====

def delete_service(service_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM servisy WHERE id = ?",
        (service_id,)
    )

    conn.commit()
    conn.close()