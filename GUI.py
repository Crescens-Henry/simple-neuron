from tkinter import filedialog
import customtkinter
import pandas as pd
import os
import numpy as np

class Frame_Input(customtkinter.CTkFrame):
    def __init__ (self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label = customtkinter.CTkLabel(self, text="ETA:")
        self.label.grid(row=0, column=0, padx=10, sticky='w')
        
        self.entry_eta = customtkinter.CTkEntry(self, placeholder_text="0.5")
        self.entry_eta.grid(row=1, column=0, padx=0)
        
        self.button_upload = customtkinter.CTkButton(self, text="Subir .CSV", command=self.upload_csv)
        self.button_upload.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky='s')
        
        self.label_response = customtkinter.CTkLabel(self, text="Seleccione un archivo", text_color="gray")
        self.label_response.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky='n')
        
        self.button_start = customtkinter.CTkButton(self, text="Iniciar", command=self.start)
        self.button_start.grid(row=4, column=0, padx=10, pady=10,)
    
    def upload_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            base_name = os.path.basename(filename)
            self.label_response.configure(text=base_name)
            self.label_response.update()
            data = pd.read_csv(filename)
            print (data)
            vector = data.values.flatten() 
            print (vector)
            num_rows = data.shape[0]
            num_cols = data.shape[1]
            matrix = np.reshape(vector, (num_rows, num_cols))
            print(matrix)
        return matrix
        
    def start(self):
        print("Starting...")