# Evidence vozového parku

Aplikace pro správu vozidel a jejich servisů s grafickým rozhraním.

## Struktura projektu
Kliknutím na název souboru se dostanete přímo ke kódu:

* [**`main.py`**](./main.py) – Hlavní vstupní bod aplikace. Inicializuje databázi a spouští GUI.
* [**`gui.py`**](./gui.py) – Definice uživatelského rozhraní (Tkinter).
* [**`database.py`**](./database.py) – Správa SQLite databáze a SQL dotazy.
* [**`validators.py`**](./validators.py) – Logika pro kontrolu správnosti zadaných dat.
* **`data/`** – Adresář obsahující soubor databáze `vozidla.db`.

## Funkce
* **Vozidla**: Evidence SPZ, značky a roku výroby.
* **Servis**: Evidence servisních úkonů (datum, popis, cena) přiřazených ke konkrétnímu vozidlu.
* **Validace**: Kontrola, zda je rok výroby reálný a zda jsou vyplněna všechna pole.

## Databázové tabulky
Aplikace využívá dvě propojené tabulky v SQLite:

1. **vozidla**: `id`, `spz`, `znacka`, `rok`
2. **servisy**: `id`, `vozidlo_id`, `datum`, `popis`, `cena`



## Instalace a spuštění
1. Ujistěte se, že máte nainstalovaný Python 3.
2. Stáhněte si soubory a ponechte strukturu složek tak, aby soubor `vozidla.db` zůstal ve složce `data`.
3. Spusťte aplikaci.
