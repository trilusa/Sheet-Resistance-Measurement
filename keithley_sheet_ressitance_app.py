import tkinter as tk
from tkinter import messagebox
import numpy as np

class Keithley2450App:
    def __init__(self, root):
        self.root = root
        self.root.title("Keithley 2450 IV Measurement")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Width (W)").grid(row=0, column=0)
        self.w_entry = tk.Entry(self.root)
        self.w_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Length (L)").grid(row=1, column=0)
        self.l_entry = tk.Entry(self.root)
        self.l_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Material").grid(row=2, column=0)
        self.material_entry = tk.Entry(self.root)
        self.material_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Number of Measurements (N)").grid(row=3, column=0)
        self.num_measurements_entry = tk.Entry(self.root)
        self.num_measurements_entry.grid(row=3, column=1)

        self.start_button = tk.Button(self.root, text="Start Measurement", command=self.start_measurement)
        self.start_button.grid(row=4, column=0, columnspan=2)

        self.results_text = tk.Text(self.root, height=10, width=50)
        self.results_text.grid(row=5, column=0, columnspan=2)

    def start_measurement(self):
        try:
            W = float(self.w_entry.get())
            L = float(self.l_entry.get())
            material = self.material_entry.get()
            N = int(self.num_measurements_entry.get())

            I_values = []
            V_values = []

            for _ in range(N):
                # Generate random measurements for offline testing
                V = np.random.randn()
                I = np.random.randn()

                V_values.append(V)
                I_values.append(I)

                mean_I = np.mean(I_values)
                std_I = np.std(I_values)
                mean_V = np.mean(V_values)
                std_V = np.std(V_values)

                self.results_text.insert(tk.END, f"Measurement {_+1}:\n")
                self.results_text.insert(tk.END, f"Mean I: {mean_I:.4e} A, Std I: {std_I:.4e} A\n")
                self.results_text.insert(tk.END, f"Mean V: {mean_V:.4e} V, Std V: {std_V:.4e} V\n")
                self.results_text.insert(tk.END, "-"*30 + "\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = Keithley2450App(root)
    root.mainloop()
