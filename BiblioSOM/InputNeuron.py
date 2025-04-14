import numpy as np

class SOM:
    def __init__(self, grid_dim, input_dim, learning_rate, radius):
        self.grid_dim = grid_dim
        self.input_dim = input_dim
        self.learning_rate = learning_rate
        self.radius = radius
        self.weight = None
        self.initialize_weights()
    
    
    def initialize_weights(self):
        self.weight = np.random.rand(self.grid_dim[0], self.grid_dim[1], self.input_dim, )
                
    def fin_bmu(self,input_vector):
        distance = np.linalg.norm(self.weight - input_vector, axis= 2)
        
        return np.unravel_index(np.argmin(distance), distance.shape)
''' TESTE DE VERIFICAÇÂO WEIGHTS     
som = SOM(grid_dim=(10,10), input_dim=(3), learning_rate=(0.5), radius=(5))
print(som.weight)
'''              
        
    
