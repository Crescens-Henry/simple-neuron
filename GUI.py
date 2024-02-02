import customtkinter
from logic import Neuron
class Frame_Input(customtkinter.CTkFrame):
    
    def __init__ (self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.neuron = Neuron()
        
        self.label = customtkinter.CTkLabel(self, text="ETA:")
        self.label.grid(row=0, column=0, padx=10, sticky='w')
        
        self.entry_eta = customtkinter.CTkEntry(self, placeholder_text="0.5")
        self.entry_eta.grid(row=1, column=0, padx=0)
        
        self.button_upload = customtkinter.CTkButton(self, text="Subir .CSV", command=lambda: self.neuron.upload_csv(self.label_response))
        self.button_upload.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky='s')
        
        self.label_response = customtkinter.CTkLabel(self, text="Seleccione un archivo", text_color="gray")
        self.label_response.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky='n')
        
        self.button_start = customtkinter.CTkButton(self, text="Iniciar", command=self.neuron.start)
        self.button_start.grid(row=4, column=0, padx=10, pady=10,)
