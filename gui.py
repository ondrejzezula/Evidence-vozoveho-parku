import tkinter as tk
from tkinter import ttk, messagebox

from database import (
    get_vehicles,
    add_vehicle,
    add_service,
    get_services_by_vehicle
)
from validators import validate_vehicle, validate_service


class VehicleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Evidence vozového parku")
        self.root.geometry("600x400")

        self.selected_vehicle_id = None

        self.create_widgets()
        self.load_vehicles()

    def create_widgets(self):

        # ===== FORMULÁŘ VOZIDLA =====
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="SPZ").grid(row=0, column=0)
        tk.Label(form_frame, text="Značka").grid(row=0, column=1)
        tk.Label(form_frame, text="Rok").grid(row=0, column=2)

        self.spz_entry = tk.Entry(form_frame)
        self.znacka_entry = tk.Entry(form_frame)
        self.rok_entry = tk.Entry(form_frame)

        self.spz_entry.grid(row=1, column=0, padx=5)
        self.znacka_entry.grid(row=1, column=1, padx=5)
        self.rok_entry.grid(row=1, column=2, padx=5)

        tk.Button(
            form_frame,
            text="Přidat vozidlo",
            command=self.add_vehicle
        ).grid(row=1, column=3, padx=10)

# ===== TLAČÍTKO SMAZAT VOZIDLO =====
        tk.Button(
            form_frame,
            text="Smazat vozidlo",
            command=self.delete_vehicle
        ).grid(row=2, column=0, columnspan=4, pady=5)


        # ===== TREEVIEW VOZIDLA =====
        self.tree = ttk.Treeview(
            self.root,
            columns=("id", "spz", "znacka", "rok"),
            show="headings"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("spz", text="SPZ")
        self.tree.heading("znacka", text="Značka")
        self.tree.heading("rok", text="Rok")

        self.tree.column("id", width=50)
        self.tree.column("spz", width=120)
        self.tree.column("znacka", width=200)
        self.tree.column("rok", width=80)

        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_vehicle_select)

        # ===== FORMULÁŘ SERVIS =====
        service_frame = tk.Frame(self.root)
        service_frame.pack(pady=10)

        tk.Label(service_frame, text="Datum (YYYY-MM-DD)").grid(row=0, column=0)
        tk.Label(service_frame, text="Popis").grid(row=0, column=1)
        tk.Label(service_frame, text="Cena").grid(row=0, column=2)

        self.date_entry = tk.Entry(service_frame)
        self.desc_entry = tk.Entry(service_frame)
        self.price_entry = tk.Entry(service_frame)

        self.date_entry.grid(row=1, column=0, padx=5)
        self.desc_entry.grid(row=1, column=1, padx=5)
        self.price_entry.grid(row=1, column=2, padx=5)

        tk.Button(
            service_frame,
            text="Přidat servis",
            command=self.add_service
        ).grid(row=1, column=3, padx=10)


# =====  TLAČÍTKO SMAZAT SERVIS =====
        tk.Button(
            service_frame,
            text="Smazat servis",
            command=self.delete_service
        ).grid(row=2, column=0, columnspan=4, pady=5)


        # ===== TREEVIEW SERVISY =====
        self.service_tree = ttk.Treeview(
            self.root,
            columns=("id", "datum", "popis", "cena"),
            show="headings"
        )

        self.service_tree.heading("id", text="ID")
        self.service_tree.heading("datum", text="Datum")
        self.service_tree.heading("popis", text="Popis")
        self.service_tree.heading("cena", text="Cena")

        self.service_tree.pack(fill=tk.BOTH, expand=True)

    def load_vehicles(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for vehicle in get_vehicles():
            self.tree.insert("", tk.END, values=vehicle)

    def add_vehicle(self):
        spz = self.spz_entry.get()
        znacka = self.znacka_entry.get()
        rok = self.rok_entry.get()

        valid, message = validate_vehicle(spz, znacka, rok)
        if not valid:
            messagebox.showerror("Chyba", message)
            return

        try:
            add_vehicle(spz, znacka, int(rok))
            self.load_vehicles()

            self.spz_entry.delete(0, tk.END)
            self.znacka_entry.delete(0, tk.END)
            self.rok_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Chyba", str(e))

    def on_vehicle_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        values = self.tree.item(selected[0])["values"]
        self.selected_vehicle_id = values[0]

        self.load_services()

    def load_services(self):
        for row in self.service_tree.get_children():
            self.service_tree.delete(row)

        if self.selected_vehicle_id is None:
            return

        for service in get_services_by_vehicle(self.selected_vehicle_id):
            self.service_tree.insert("", tk.END, values=service)

    def add_service(self):
        if self.selected_vehicle_id is None:
            messagebox.showerror("Chyba", "Vyberte vozidlo.")
            return

        datum = self.date_entry.get()
        popis = self.desc_entry.get()
        cena = self.price_entry.get()

        valid, message = validate_service(datum, popis, cena)
        if not valid:
            messagebox.showerror("Chyba", message)
            return

        add_service(self.selected_vehicle_id, datum, popis, float(cena))
        self.load_services()

        self.date_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
