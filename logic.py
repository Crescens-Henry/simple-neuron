import random
import numpy as np

class Neuron:
    def __init__(self, eta, epochs, data):
        self.data = data
        self.eta = eta
        self.epochs = epochs
        self.Ydesired = self.data[:, -1]
        self.W = []
        self.all_weights = []
        self.list_epoch = []
    
    def calculate_weights(self):
        self.W = np.array(
            [1 if i == 0 else float(f"{random.uniform(0, 1):.2f}") for i in range(self.data.shape[1] - 1)])
    
    def add_bias(self):
        ones_columns = np.ones((self.data.shape[0], 1))
        self.data = np.hstack((ones_columns, self.data))

    def step_function(self, u):
        result = []
        for x in u:
            if x >= 0:
                result.append(1)
            else:
                result.append(0)
        return result
        
    
    def start_optimization(self):
        self.add_bias()
        self.calculate_weights()
        for epoch in range(self.epochs):
            u = np.linalg.multi_dot([self.data[:, 1:-1], np.transpose(self.W[1:])]) + self.W[0]
            errors = np.array(self.Ydesired - self.step_function(u))
            delta = self.delta(errors)
            norm_error = np.linalg.norm(errors)
            self.all_weights.append(self.W)
            epoch_info = {
                "id": epoch,
                "norm_error": norm_error,
                "weights": self.W.tolist(), 
                "all_weights": [w.tolist() for w in self.all_weights] 
            }
            self.list_epoch.append(epoch_info)
            self.update_weights(delta)
    def delta(self, error):
        return self.eta * np.dot(np.transpose(error), self.data[:, :-1])
    
    def update_weights(self, delta_x):
        self.W = np.round(np.add(self.W, delta_x), 4)
    
    def get_initial_weights(self):
        return self.all_weights[0][1:] if self.all_weights else None

    def get_final_weights(self):
        return self.all_weights[-1][1:] if self.all_weights else None
