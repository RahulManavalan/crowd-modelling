import numpy as np 
from utils import parse_file,visualize,parse_tensor_file
import matplotlib.pyplot as plt


""" 
Represents a 2D cartesian grid. 
"""
class Grid2D: 
    def __init__(self,filename:str): 
        domain = parse_file(filename); 
        self.nrows = domain.shape[0];
        self.ncols = domain.shape[1]; 
        self.data = domain; 
        self.target = np.where(domain==3);
                
    def visualize(self):
        # include function for 2d 
        return 

class Grid3D: 
    def __init(self,filename:str): 
        domain = parse_tensor_file(filename);
        self.ndims = domain.ndims; 
        self.nrows = domain.shape[0]; 
        self.ncols = domain.shape[1]; 
        self.data = domain; 
        self.target = np.where(domain == 3);

    def visualize(self):
        # inlcude function for 3d visualization
        return 

# Include more objects for 2d grid and 3d grid respectively. 
