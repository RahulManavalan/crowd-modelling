import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt 
from grid import Grid2D,Grid3D 
from update import update2_domain,update3_domain

class Simulation2D: 
    def __init__(self,grid:Grid2D,n_time:int): 
        self.grid = grid;
        self.n = n_time;
    def solve(self): 
        for i in range(self.n): 
            new_domain = deepcopy(self.domain);
            self.domain = update2_domain(new_domain);

class Simulation3D: 
    def __init__(self,grid:Grid3D,n_time:int): 
        self.grid = grid; 
        self.n = n_time; 
    def solve(self): 
        for i in range(self.n): 
            new_domain = deepcopy(self.domain); 
            self.domain = update3_domain(new_domain); 
