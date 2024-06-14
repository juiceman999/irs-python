import customtkinter as ctk
from tkinter import Frame

def create_home_frame(parent, user_info):
    frame = ctk.CTkFrame(parent)
    welcome_label = ctk.CTkLabel(frame, text=f"Bienvenue {user_info['first_name']}!", font=("Arial", 20))
    welcome_label.pack(pady=20)
    return frame
