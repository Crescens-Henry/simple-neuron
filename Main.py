import customtkinter
from GUI import Frame_Input

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Sample Neuron')
        self.geometry('650x300')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.my_frame = Frame_Input(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

app = App()
app.mainloop()