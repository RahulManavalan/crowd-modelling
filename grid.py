from utils import parse_file,find_neighbour,find_state
from cell import *
from copy import deepcopy

class DCSProblem: 
    def __init__(self,filename:str): 
        #  All this data remains constant 
        self.domain = parse_file(filename);
        self.nrows = self.domain.shape[0]; 
        self.ncols = self.domain.shape[1];
        self.target = np.argwhere(self.domain==3);  
        
        # All of this mutable 
        self.pedestrians = np.argwhere(self.domain==1);
        self.grid = [];
        N = []; 
        S = [];
        for i in range(self.nrows):
            LN = [];
            LS = [];
            l_grid = []; 
            for j in range(self.ncols): 
                neigh = find_neighbour(i,j,self.nrows,self.ncols); 
                state = find_state(self.domain[i][j]);
                l_grid.append(Cell(i,j,state,neigh));
                LN.append(neigh); LS.append(state);
            N.append(LN);
            S.append(LS);
            self.grid.append(l_grid);
        
    def simulate(self,nsteps:int):
        for it in range(nsteps):
            new_grid = deepcopy(self.grid);
            for pedes in self.pedestrians:
                i = pedes[0]; 
                j = pedes[1]; 
                if(tuple(self.target[0]) in self.grid[i][j].neighbours):
                    break; 
                else: 
                    self.grid[i][j].distance_to_target(self.target[0]);
                loc = np.argwhere(self.grid[i][j].nd2target == np.min(self.grid[i][j].nd2target));
                next_site = self.grid[i][j].neighbours[loc[0][0]]
                new_grid[i][j].state = Type.Empty;
                new_grid[next_site[0]][next_site[1]].state = Type.Pedestrian;
                # Conditional statements gallore
            self.grid = new_grid;

    def print(self):
        for i in range(self.nrows):
            for j in range(self.ncols):
                print_cell(self.grid[i][j]);
    
    def pprint(self):
        for i in range(self.nrows):
            for j in range(self.ncols):
                if(self.grid[i][j].state==Type.Pedestrian):
                    print("p",end=" ");
                elif(self.grid[i][j].state==Type.Obstacle): 
                    print("o",end=" "); 
                elif(self.grid[i][j].state==Type.Target):
                    print("t",end=" ");
                elif(self.grid[i][j].state==Type.Empty):
                    print("+",end=" "); 
            print("\n",end="")
        