import customtkinter as ctk
from tkinter import Frame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Mock data for demonstration purposes
weight_history = [
    ("2024-01-01", 70),
    ("2024-02-01", 71),
    ("2024-03-01", 72),
    ("2024-04-01", 71),
    ("2024-05-01", 70)
]

def create_stats_frame(parent):
    frame = ctk.CTkFrame(parent)

    def plot_weight_history():
        dates = [row[0] for row in weight_history]
        weights = [row[1] for row in weight_history]

        fig, ax = plt.subplots()
        ax.plot(dates, weights, marker='o')
        ax.set(xlabel='Date', ylabel='Weight (kg)', title='Weight History')
        ax.grid()

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    plot_weight_history()
    return frame
