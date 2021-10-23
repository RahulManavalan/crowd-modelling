import numpy as np
from utils import *
from cell import *

def test_parse_file(): 
    filename = "grid_pattern.dat"; 
    domain = parse_file(filename);
    print(np.argwhere(domain==2));
    print(domain)

def test_find_state():
    filename = "grid_pattern.dat";
    domain = parse_file(filename); 
    for i in range(domain.shape[0]): 
        for j in range(domain.shape[1]): 
            print(find_state(domain[i][j]));
        print("\n");

def test_neighbours(): 
    filename = "grid_pattern.dat";
    domain = parse_file(filename); 
    for i in range(domain.shape[0]): 
        for j in range(domain.shape[1]):
            print(find_neighbour(i,j,domain.shape[0],domain.shape[1]));
        print("-----------------------------------------"); 
    
def test_cell(): 
    filename = "grid_pattern.dat";
    domain = parse_file(filename);
    grid = [];
    for i in range(domain.shape[0]):
        l_grid = []; 
        for j in range(domain.shape[1]): 
            neigh = find_neighbour(i,j,domain.shape[0],domain.shape[1]);
            state = find_state(domain[i][j]);
            l_grid.append(Cell(i,j,state,neigh));
        grid.append(l_grid);
    print_grid(grid);
        

def main():
    test_parse_file(); 
    # test_find_state();
    # test_neighbours();
    # test_cell();

main();