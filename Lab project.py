import tkinter as tk
from tkinter import ttk, messagebox
import os

# =====================================
# COLOR THEME
# =====================================

BG_COLOR = "#0f172a"
TAB_COLOR = "#1e293b"
BTN_BLUE = "#3b82f6"
BTN_GREEN = "#22c55e"
TEXT_COLOR = "white"


# =====================================
# BACKEND CLASSES
# =====================================

class Camp:

    def __init__(self, camp_id, location, capacity):

        self.camp_id = camp_id
        self.location = location
        self.capacity = capacity
        self.occupancy = 0
        self.food = 0
        self.medical = 0
        self.volunteers = 0

    def is_full(self):
        return self.occupancy >= self.capacity

    def to_string(self):

        return f"{self.camp_id}|{self.location}|{self.capacity}|{self.occupancy}|{self.food}|{self.medical}|{self.volunteers}"

    @staticmethod
    def from_string(line):

        parts = line.strip().split("|")

        camp = Camp(parts[0], parts[1], int(parts[2]))

        camp.occupancy = int(parts[3])
        camp.food = int(parts[4])
        camp.medical = int(parts[5])
        camp.volunteers = int(parts[6])

        return camp


class Victim:

    def __init__(self, vid, name, age, health, camp_id):

        self.vid = vid
        self.name = name
        self.age = age
        self.health = health
        self.camp_id = camp_id

    def to_string(self):

        return f"{self.vid}|{self.name}|{self.age}|{self.health}|{self.camp_id}"

    @staticmethod
    def from_string(line):

        parts = line.strip().split("|")

        return Victim(parts[0], parts[1], parts[2], parts[3], parts[4])


class DisasterReliefSystem:

    def __init__(self):

        self.camps = []
        self.victims = []

        self.camp_file = "camps.txt"
        self.victim_file = "victims.txt"

        self.load()

    def load(self):

        if os.path.exists(self.camp_file):

            with open(self.camp_file) as f:

                for line in f:
                    self.camps.append(Camp.from_string(line))

        if os.path.exists(self.victim_file):

            with open(self.victim_file) as f:

                for line in f:
                    self.victims.append(Victim.from_string(line))

    def save(self):

        with open(self.camp_file, "w") as f:

            for camp in self.camps:
                f.write(camp.to_string()+"\n")

        with open(self.victim_file, "w") as f:

            for victim in self.victims:
                f.write(victim.to_string()+"\n")

    def add_camp(self, cid, loc, cap, food, medical, vol):

        for camp in self.camps:
            if camp.camp_id == cid:
                return False

        camp = Camp(cid, loc, cap)
        camp.food = food
        camp.medical = medical
        camp.volunteers = vol

        self.camps.append(camp)

        self.save()

        return True

    def register_victim(self, vid, name, age, health, camp_id):

        for v in self.victims:
            if v.vid == vid:
                return False

        camp = self.find_camp(camp_id)

        if camp is None or camp.is_full():
            return False

        victim = Victim(vid, name, age, health, camp_id)

        self.victims.append(victim)

        camp.occupancy += 1

        self.save()

        return True

    def find_camp(self, cid):

        for camp in self.camps:

            if camp.camp_id == cid:
                return camp

        return None


# =====================================
# GUI
# =====================================

system = DisasterReliefSystem()

root = tk.Tk()

root.title("Smart Disaster Relief System")

root.geometry("900x600")

root.configure(bg=BG_COLOR)


# =====================================
# NOTEBOOK (TAB UI)
# =====================================

notebook = ttk.Notebook(root)

notebook.pack(fill="both", expand=True)


# =====================================
# DASHBOARD TAB
# =====================================

dashboard = tk.Frame(notebook, bg=BG_COLOR)

notebook.add(dashboard, text="Dashboard")

title = tk.Label(

    dashboard,
    text="SMART DISASTER RELIEF SYSTEM",
    font=("Segoe UI", 24, "bold"),
    bg=BG_COLOR,
    fg="#22c55e"
)

title.pack(pady=20)

info = tk.Label(

    dashboard,
    font=("Segoe UI", 16),
    bg=BG_COLOR,
    fg="white"
)

info.pack()


def update_dashboard():

    info.config(

        text=f"Total Camps: {len(system.camps)}\nTotal Victims: {len(system.victims)}"
    )


update_dashboard()


# =====================================
# ADD CAMP TAB
# =====================================

addcamp = tk.Frame(notebook, bg=TAB_COLOR)

notebook.add(addcamp, text="Add Camp")

entries = {}

fields = ["Camp ID", "Location", "Capacity", "Food", "Medical", "Volunteers"]

for field in fields:

    tk.Label(

        addcamp,
        text=field,
        bg=TAB_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 12)

    ).pack()

    entry = tk.Entry(addcamp, font=("Segoe UI", 12))

    entry.pack(pady=5)

    entries[field] = entry


def add_camp():

    ok = system.add_camp(

        entries["Camp ID"].get(),
        entries["Location"].get(),
        int(entries["Capacity"].get()),
        int(entries["Food"].get()),
        int(entries["Medical"].get()),
        int(entries["Volunteers"].get())

    )

    if ok:

        messagebox.showinfo("Success", "Camp Added")

        update_dashboard()

        load_camps()

    else:

        messagebox.showerror("Error", "Camp exists")


tk.Button(

    addcamp,
    text="Add Camp",
    bg=BTN_BLUE,
    fg="white",
    font=("Segoe UI", 12),
    command=add_camp

).pack(pady=10)


# =====================================
# REGISTER VICTIM TAB
# =====================================

victimtab = tk.Frame(notebook, bg=TAB_COLOR)

notebook.add(victimtab, text="Register Victim")

ventries = {}

fields2 = ["Victim ID", "Name", "Age", "Health", "Camp ID"]

for field in fields2:

    tk.Label(

        victimtab,
        text=field,
        bg=TAB_COLOR,
        fg=TEXT_COLOR,
        font=("Segoe UI", 12)

    ).pack()

    entry = tk.Entry(victimtab, font=("Segoe UI", 12))

    entry.pack(pady=5)

    ventries[field] = entry


def register():

    ok = system.register_victim(

        ventries["Victim ID"].get(),
        ventries["Name"].get(),
        ventries["Age"].get(),
        ventries["Health"].get(),
        ventries["Camp ID"].get()

    )

    if ok:

        messagebox.showinfo("Success", "Victim Registered")

        update_dashboard()

        load_victims()

    else:

        messagebox.showerror("Error", "Registration Failed")


tk.Button(

    victimtab,
    text="Register Victim",
    bg=BTN_GREEN,
    fg="white",
    font=("Segoe UI", 12),
    command=register

).pack(pady=10)


# =====================================
# VIEW CAMPS TAB
# =====================================

campview = tk.Frame(notebook)

notebook.add(campview, text="View Camps")

camp_tree = ttk.Treeview(campview)

camp_tree["columns"] = ("ID", "Location", "Capacity", "Occupancy")

for col in camp_tree["columns"]:
    camp_tree.heading(col, text=col)

camp_tree["show"] = "headings"

camp_tree.pack(fill="both", expand=True)


def load_camps():

    for row in camp_tree.get_children():
        camp_tree.delete(row)

    for camp in system.camps:

        camp_tree.insert("", "end", values=(

            camp.camp_id,
            camp.location,
            camp.capacity,
            camp.occupancy

        ))


load_camps()


# =====================================
# VIEW VICTIMS TAB
# =====================================

victimview = tk.Frame(notebook)

notebook.add(victimview, text="View Victims")

victim_tree = ttk.Treeview(victimview)

victim_tree["columns"] = ("ID", "Name", "Age", "Health", "Camp")

for col in victim_tree["columns"]:
    victim_tree.heading(col, text=col)

victim_tree["show"] = "headings"

victim_tree.pack(fill="both", expand=True)


def load_victims():

    for row in victim_tree.get_children():
        victim_tree.delete(row)

    for v in system.victims:

        victim_tree.insert("", "end", values=(

            v.vid,
            v.name,
            v.age,
            v.health,
            v.camp_id

        ))


load_victims()

root.mainloop()