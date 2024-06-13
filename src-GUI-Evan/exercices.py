import customtkinter as ctk
from tkinter import Frame, Listbox, Toplevel, Text, END, StringVar, BOTH

machines = [
    {"name": "Tapis de course", "body_parts": ["Cardio"], "description": "Pour la course et la marche.", "video": "url_video_tapis_de_course"},
    {"name": "Vélo elliptique", "body_parts": ["Cardio"], "description": "Pour un entraînement cardio à faible impact.", "video": "url_video_elliptique"},
    # Ajouter d'autres machines ici
]

def create_exercises_frame(parent):
    frame = ctk.CTkFrame(parent)
    frame.pack(fill=BOTH, expand=True)

    filter_var = StringVar()
    filter_entry = ctk.CTkEntry(frame, textvariable=filter_var)
    filter_entry.grid(row=0, column=0, padx=10, pady=10)

    def filter_machines():
        query = filter_var.get().lower()
        filtered_machines = [m for m in machines if query in m["name"].lower() or any(query in bp.lower() for bp in m["body_parts"])]
        update_machines_list(filtered_machines)

    ctk.CTkButton(frame, text="Filtrer", command=filter_machines).grid(row=0, column=1, padx=10, pady=10)

    listbox = Listbox(frame)
    listbox.grid(row=1, column=0, columnspan=2, sticky="nsew")
    listbox.bind('<<ListboxSelect>>', lambda event: show_machine_details(listbox.get(listbox.curselection())))

    def update_machines_list(machines_to_display):
        listbox.delete(0, END)
        for machine in machines_to_display:
            listbox.insert(END, machine["name"])

    def show_machine_details(machine_name):
        for machine in machines:
            if machine["name"] == machine_name:
                machine_window = Toplevel()
                machine_window.title(machine_name)
                description = Text(machine_window, height=10)
                description.pack()
                description.insert(END, f"Description: {machine['description']}\n")
                description.insert(END, f"Video: {machine['video']}\n")

    update_machines_list(machines)
    return frame
