# Evidence vozového parku

Aplikace pro správu vozidel a jejich servisů s grafickým rozhraním a modulem pro výpočet nákladů.

## Struktura projektu
Kliknutím na název souboru se dostanete přímo ke kódu:

* [**`main.py`**](./main.py) – Hlavní vstupní bod aplikace. Inicializuje databázi a spouští uživatelské rozhraní.
* [**`gui.py`**](./gui.py) – Definice grafického rozhraní (Tkinter) a obsluha tlačítek.
* [**`database.py`**](./database.py) – Kompletní správa SQLite databáze a SQL dotazy.
* [**`vypocty.py`**](./vypocty.py) – Modul pro analýzu dat (celkové náklady, průměry, filtrování období).
* [**`validators.py`**](./validators.py) – Funkce pro kontrolu správnosti zadávaných údajů.
* **`data/`** – Složka pro uložení databázového souboru `vozidla.db`.
* **`__pycache__/`** – Systémová složka s kompilovanými soubory Pythonu (není třeba upravovat).

## Funkce
* **Evidence vozidel**: Přidávání a mazání aut (SPZ, značka, rok výroby).
* **Servisní historie**: Evidence konkrétních servisních úkonů ke každému vozu.
* **Statistiky a výpočty**:
    * Celkové náklady za celý vozový park.
    * Součet nákladů pro konkrétní vozidlo.
    * Průměrná cena jednoho servisu.
    * Celkové náklady za zvolené časové období.
* **Ochrana dat**: Validace vstupů (kontrola číselných hodnot a formátů dat).

## Databáze
Aplikace využívá dvě tabulky:
1. **vozidla**: (id, spz, znacka, rok)
2. **servisy**: (id, vozidlo_id, datum, popis, cena)


## Jak aplikaci spustit
1. Ujistěte se, že máte v adresáři složku `data`.
2. V terminálu/příkazovém řádku spusťte
