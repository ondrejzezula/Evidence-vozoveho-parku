# Evidence vozového parku

Aplikace pro správu vozidel a jejich servisů s grafickým rozhraním a pokročilými statistikami nákladů.

## Struktura projektu
Kliknutím na název souboru se dostanete přímo ke kódu:

* [**`main.py`**](./main.py) – Hlavní vstupní bod aplikace. Inicializuje databázi a spouští GUI.
* [**`gui.py`**](./gui.py) – Definice uživatelského rozhraní (Tkinter).
* [**`database.py`**](./database.py) – Správa SQLite databáze a SQL dotazy pro CRUD operace.
* [**`stats.py`**](./stats.py) – (Nový) Modul pro výpočty nákladů a statistik z databáze.
* [**`validators.py`**](./validators.py) – Logika pro kontrolu správnosti zadaných dat.
* **`data/`** – Adresář obsahující soubor databáze `vozidla.db`.

## Funkce
* **Vozidla**: Evidence SPZ, značky a roku výroby.
* **Servis**: Evidence servisních úkonů (datum, popis, cena) přiřazených k vozidlu.
* **Validace**: Kontrola reálnosti roku výroby a povinných polí.
* **Statistiky nákladů**: 
    * Výpočet celkových nákladů celého vozového parku.
    * Náklady na konkrétní vybrané vozidlo.
    * Filtrování nákladů podle časového období (od-do).
    * Výpočet průměrné ceny za jeden servisní úkon.

## Databázové tabulky
Aplikace využívá dvě propojené tabulky v SQLite:

1. **vozidla**: `id`, `spz`, `znacka`, `rok`
2. **servisy**: `id`, `vozidlo_id`, `datum`, `popis`, `cena`



## 🚀 Instalace a spuštění
1. Ujistěte se, že máte nainstalovaný Python 3.
2. Stáhněte si soubory a zachovejte strukturu složek (databáze musí být v `/data`).
3. Spusťte aplikaci.
