import numpy as np
from type import Type

class Cell: 
    def __init__(self,i:int,j:int,state:Type,neigh:list): 
        self.i = i; 
        self.j = j;
        self.state = state;
        self.neighbours = neigh;
        self.velocity = None;
        self.nd2target = [];

    def distance_to_target(self,tidx:list): 
       for neigh in self.neighbours: 
           self.nd2target.append(np.sqrt((neigh[0]-tidx[0])**2+(neigh[1]-tidx[1])**2));
    
def print_cell(cell:Cell): 
    print(cell.i);
    print(cell.j);
    print(cell.state)
    print(cell.neighbours)

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])): 
            print_cell(grid[i][j]);
            print("--------------------------------");