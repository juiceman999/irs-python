import customtkinter as ctk
from tkinter import Frame, Scrollbar, LEFT, BOTH, RIGHT, Y, StringVar, END
from datetime import datetime

def create_personal_info_frame(parent, user_info):
    frame = ctk.CTkFrame(parent)
    personal_info_canvas = ctk.CTkCanvas(frame)
    personal_info_scrollbar = Scrollbar(frame, orient="vertical", command=personal_info_canvas.yview)
    personal_info_canvas.configure(yscrollcommand=personal_info_scrollbar.set)
    personal_info_canvas.bind('<Configure>', lambda e: personal_info_canvas.configure(scrollregion=personal_info_canvas.bbox("all")))
    personal_info_container = ctk.CTkFrame(personal_info_canvas)
    personal_info_canvas.create_window((0, 0), window=personal_info_container, anchor="nw")
    personal_info_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    personal_info_scrollbar.pack(side=RIGHT, fill=Y)
    create_personal_info_subcategories(personal_info_container, user_info)
    return frame

def create_personal_info_subcategories(container, user_info):
    buttons = [
        ("Santé", lambda: show_health_info(health_frame, muscle_stats_frame)),
        ("Stats Personnelles", lambda: show_muscle_stats(health_frame, muscle_stats_frame))
    ]

    for text, command in buttons:
        ctk.CTkButton(container, text=text, command=command).pack(pady=5)

    health_frame = create_health_widgets(container, user_info)
    muscle_stats_frame = create_muscle_stats_widgets(container)
    show_health_info(health_frame, muscle_stats_frame)

def create_health_widgets(container, user_info):
    frame = ctk.CTkFrame(container)  # Supprimé borderwidth et relief
    fields = [
        ("Poids (kg):", "weight"),
        ("Taille (cm):", "height"),
        ("Âge:", "age"),
        ("Sexe:", "gender", ["Homme", "Femme"]),
        ("Objectif:", "objective", ["Prise de masse", "Perte de poids"])
    ]

    for row, (label_text, key, *options) in enumerate(fields):
        ctk.CTkLabel(frame, text=label_text).grid(row=row, column=0, pady=10, padx=10)
        if options:
            var = StringVar(value=user_info[key])
            ctk.CTkOptionMenu(frame, variable=var, values=options[0]).grid(row=row, column=1, pady=10, padx=10)
            setattr(frame, f"{key}_var", var)
        else:
            entry = ctk.CTkEntry(frame)
            entry.grid(row=row, column=1, pady=10, padx=10)
            entry_value = str(user_info.get(key, ""))  # Convertir en chaîne de caractères si nécessaire
            entry.insert(0, entry_value)
            setattr(frame, f"{key}_entry", entry)

    add_additional_health_widgets(frame, user_info)
    return frame

def add_additional_health_widgets(frame, user_info):
    ctk.CTkButton(frame, text="Calculer IMC", command=lambda: calculate_bmi(frame, user_info)).grid(row=5, column=0, columnspan=2, pady=10)

    ctk.CTkLabel(frame, text="Votre IMC est :").grid(row=6, column=0, pady=10, padx=10)
    bmi_result = ctk.CTkEntry(frame)
    bmi_result.grid(row=6, column=1, pady=10, padx=10)
    frame.bmi_result = bmi_result

    ctk.CTkLabel(frame, text="Poids idéal :").grid(row=7, column=0, pady=10, padx=10)
    ideal_weight_result = ctk.CTkEntry(frame)
    ideal_weight_result.grid(row=7, column=1, pady=10, padx=10)
    frame.ideal_weight_result = ideal_weight_result

    ctk.CTkLabel(frame, text="Catégorie IMC :").grid(row=8, column=0, pady=10, padx=10)
    bmi_category = ctk.CTkLabel(frame, text="")
    bmi_category.grid(row=8, column=1, pady=10, padx=10)
    frame.bmi_category = bmi_category

    bmi_gauge = ctk.CTkProgressBar(frame, orientation='horizontal', mode='determinate')
    bmi_gauge.grid(row=9, column=0, columnspan=2, pady=10, padx=10)
    frame.bmi_gauge = bmi_gauge
    bmi_gauge.set(0)

def calculate_bmi(frame, user_info):
    weight = float(frame.weight_entry.get())
    height = float(frame.height_entry.get()) / 100
    bmi = weight / (height ** 2)
    gender = frame.gender_var.get()
    ideal_weight = calculate_ideal_weight(height * 100, gender)

    frame.bmi_result.delete(0, 'end')
    frame.bmi_result.insert(0, f"{bmi:.2f}")

    frame.ideal_weight_result.delete(0, 'end')
    frame.ideal_weight_result.insert(0, f"{ideal_weight:.2f}")

    update_bmi_gauge(frame, bmi, gender)

def calculate_ideal_weight(height, gender):
    return height - 100 - ((height - 150) / 4) if gender == "Homme" else height - 100 - ((height - 150) / 2.5)

def update_bmi_gauge(frame, bmi, gender):
    categories = [
        ("Sous-poids", 18.5),
        ("Normal", 24.9),
        ("Parfait", 25),
        ("Surpoids", 29.9),
        ("Obèse", float('inf'))
    ]
    colors = ["blue", "green", "lightgreen", "yellow", "red"]

    category_index = 0
    for i, (category, upper_bound) in enumerate(categories):
        if bmi <= upper_bound:
            category_index = i
            break

    frame.bmi_category.configure(text=categories[category_index][0])
    frame.bmi_gauge.set(category_index / len(categories))
    frame.bmi_gauge.configure(fg_color=colors[category_index])

def create_muscle_stats_widgets(container):
    frame = ctk.CTkFrame(container)  # Supprimé borderwidth et relief
    fields = [
        ("Tour de Cou (cm):", "neck"),
        ("Tour de Poitrine (cm):", "chest"),
        ("Tour de Taille (cm):", "waist"),
        ("Tour de Hanches (cm):", "hips"),
        ("Tour de Cuisse (cm):", "thigh"),
        ("Tour de Mollet (cm):", "calf"),
        ("Tour de Biceps (cm):", "biceps"),
        ("Tour d'Avant-bras (cm):", "forearm"),
        ("Tour de Poignet (cm):", "wrist"),
        ("Tour d'Épaules (cm):", "shoulder")
    ]

    entries = {}
    for row, (label_text, key) in enumerate(fields):
        ctk.CTkLabel(frame, text=label_text).grid(row=row, column=0, pady=10, padx=10)
        entry = ctk.CTkEntry(frame)
        entry.grid(row=row, column=1, pady=10, padx=10)
        entries[key] = entry
    
    ctk.CTkButton(frame, text="Enregistrer", command=lambda: save_muscle_stats(entries)).grid(row=len(fields), column=0, columnspan=2, pady=10)
    ctk.CTkButton(frame, text="Afficher l'historique", command=show_stats_history).grid(row=len(fields)+1, column=0, columnspan=2, pady=10)

    return frame

def save_muscle_stats(entries):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {key: float(entry.get()) for key, entry in entries.items()}
    data['date'] = current_date
    # Logique pour enregistrer les données dans un fichier ou une base de données

def show_stats_history():
    history_window = ctk.CTkToplevel()
    history_window.title("Historique des Mensurations")
    history_window.geometry("600x400")

    listbox = ctk.CTkListbox(history_window)
    listbox.pack(fill=BOTH, expand=True)

    # Logique pour afficher l'historique des mensurations
    history_data = []  # Remplacer par les données réelles
    for row in history_data:
        listbox.insert(END, f"Date: {row['date']}, Cou: {row['neck']} cm, Poitrine: {row['chest']} cm, Taille: {row['waist']} cm, Hanches: {row['hips']} cm, Cuisse: {row['thigh']} cm, Mollet: {row['calf']} cm, Biceps: {row['biceps']} cm, Avant-bras: {row['forearm']} cm, Poignet: {row['wrist']} cm, Épaules: {row['shoulder']} cm")

def show_health_info(health_frame, muscle_stats_frame):
    muscle_stats_frame.pack_forget()
    health_frame.pack(pady=10, padx=10, fill="x")

def show_muscle_stats(health_frame, muscle_stats_frame):
    health_frame.pack_forget()
    muscle_stats_frame.pack(pady=10, padx=10, fill="x")
