import os
from tkinter import filedialog
import customtkinter
import pandas as pd
import Plots

from logic import Neuron

class Frame_Input(customtkinter.CTkFrame):
    
    def __init__ (self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.data = None
        
        self.button_upload = customtkinter.CTkButton(self, text="Subir .CSV", command=self.upload_csv)
        self.button_upload.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='s')
        
        self.label_response = customtkinter.CTkLabel(self, text="Seleccione un archivo", text_color="gray")
        self.label_response.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='n')
        
        self.label = customtkinter.CTkLabel(self, text="ETA:")
        self.label.grid(row=2, column=0, padx=10, sticky='w')
        
        self.entry_eta = customtkinter.CTkEntry(self, placeholder_text="0.5")
        self.entry_eta.grid(row=3, column=0, padx=0)
        
        self.label_epochs = customtkinter.CTkLabel(self, text="Epochs:")
        self.label_epochs.grid(row=4, column=0, padx=10, sticky='w')
        
        self.entry_epochs = customtkinter.CTkEntry(self, placeholder_text="100")
        self.entry_epochs.grid(row=5, column=0, padx=0)
        
        self.entry_eta.insert(0, "0.5")
        self.entry_epochs.insert(0, "100")
        
        self.button_start = customtkinter.CTkButton(self, text="Iniciar", command=self.button_start)
        self.button_start.grid(row=6, column=0, padx=10, pady=10,)

    def upload_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            base_name = os.path.basename(filename)
            self.label_response.configure(text=base_name)
            self.label_response.update()
            data = pd.read_csv(filename, sep=";")
        self.data = data.values
        
    def button_start(self):
        try:
            data = self.data
            if data is not None:
                neuron = Neuron(float(self.entry_eta.get()), int(self.entry_epochs.get()), data)
                neuron.start_optimization()
                Plots.plot_data(neuron.list_epoch)
        except Exception as e:
            print(f"An error occurred: {e}")