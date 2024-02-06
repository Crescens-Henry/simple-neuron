import os
from tkinter import filedialog
import customtkinter
import pandas as pd
import Plots

from logic import Neuron
from pandas.errors import EmptyDataError

class Frame_Input(customtkinter.CTkFrame):
    
    def __init__ (self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.data = None
        
        self.button_upload = customtkinter.CTkButton(self, text="Subir .CSV", command=self.upload_csv)
        self.button_upload.grid(row=0, column=0, padx=10, pady=10, sticky='s')
        
        self.label_response = customtkinter.CTkLabel(self, text="Seleccione un archivo . CSV", text_color="gray")
        self.label_response.grid(row=1, column=0, padx=10, pady=10, sticky='n')
        
        self.label = customtkinter.CTkLabel(self, text="Taza de aprendizaje(ETA):")
        self.label.grid(row=2, column=0, padx=10, sticky='w')
        
        self.entry_eta = customtkinter.CTkEntry(self, placeholder_text="0.5")
        self.entry_eta.grid(row=3, column=0, padx=10)
        
        self.label_epochs = customtkinter.CTkLabel(self, text="Numero de Epocas:")
        self.label_epochs.grid(row=4, column=0, padx=10, sticky='w')
        
        self.entry_epochs = customtkinter.CTkEntry(self, placeholder_text="100")
        self.entry_epochs.grid(row=5, column=0, padx=10)
        
        self.entry_eta.insert(0, "0.000001")
        self.entry_epochs.insert(0, "100")
        
        self.button_start = customtkinter.CTkButton(self, text="Iniciar", command=self.button_start)
        self.button_start.grid(row=6, column=0, padx=10, pady=10,)
        
        self.result_text = customtkinter.CTkTextbox(self, border_width=2, width=400)
        self.result_text.grid(row=0, column=1, padx=10, pady=10,rowspan=10, columnspan=10, sticky='nsew')

    def upload_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            base_name = os.path.basename(filename)
            self.label_response.configure(text=f"{base_name}\nCargado exitosamente", text_color="green")
            self.label_response.update()
            try:
                data = pd.read_csv(filename, sep=";")
                self.button_start.configure(state="enabled")
            except EmptyDataError:
                self.label_response.configure(text="El archivo esta vacio\nintente con otro", text_color="red")
                self.label_response.update()
                self.button_start.configure(state="disabled")
                return
            except Exception as e:
                self.label_response.configure(text=f"Error: {e}", text_color="red")
                self.label_response.update()
                return
        self.data = data.values
        
    def button_start(self):
        try:
            data = self.data
            if data is not None:
                neuron = Neuron(float(self.entry_eta.get()), int(self.entry_epochs.get()), data)
                neuron.start_optimization()
                self.result_text.delete(1.0, 'end')
                final_norm = neuron.list_epoch[-1]['norm_error']
                initial_weights = neuron.get_initial_weights()
                final_weights = neuron.get_final_weights()
                iterations = len(neuron.list_epoch)  


                results = f"Tasa de aprendizaje (eta): {self.entry_eta.get()}\n"
                results += f"Error Permisible: {final_norm}\n"
                results += f"Cantidad de Epocas: {iterations}\n\n"
                results += f"Pesos iniciales de w: {initial_weights}\n"
                results += f"Pesos finales de w: {final_weights}\n"

                self.result_text.insert('end', results)
                Plots.plot_data(neuron.list_epoch)
        except Exception as e:
            print(f"An error occurred: {e}")