import tkinter as tk
from database import create_tables
from gui import VehicleApp

if __name__ == "__main__":
    create_tables()

    root = tk.Tk()
    app = VehicleApp(root)
    root.mainloop()