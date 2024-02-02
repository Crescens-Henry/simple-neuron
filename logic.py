from tkinter import filedialog
import pandas as pd
import os
import numpy as np


class Neuron:
    def __init__(self):
        self.matrix = None
    
    def upload_csv(self, label_response):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            base_name = os.path.basename(filename)
            label_response.configure(text=base_name)
            label_response.update()
            data = pd.read_csv(filename)
            vector = data.values.flatten() 
            num_rows = data.shape[0]
            num_cols = data.shape[1]
            self.matrix = np.reshape(vector, (num_rows, num_cols))
    
    def start(self):
        if self.matrix is not None:
            print("Starting...")
        else:
            print("No matrix loaded")