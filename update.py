from typing import Tuple
import numpy as np 
from copy import deepcopy

def get_neighbours(domain:np.ndarray.dtype,s:tuple): 
    neighbours = []; 
    neighbours.append(domain[s[0]+1][s[1]]); # Right  
    neighbours.append(domain[s[0]-1][s[1]]); # Left 
    neighbours.append(domain[s[0]][s[1]+1]); # Top 
    neighbours.append(domain[s[0]][s[1]-1]); # Bottom 
    neighbours.append(domain[s[0]+1][s[1]+1]); # Top Right 
    neighbours.append(domain[s[0]+1][s[1]-1]); # Bottom Right 
    neighbours.append(domain[s[0]-1][s[1]+1]); # Top Left
    neighbours.append(domain[s[0]-1][s[1]-1]); # Bottom Left
    return neighbours; 

def distance_to_target(elem:tuple,domain:np.ndarray.dtype,target:tuple): 
    i = target[0];
    j = target[1]; 
    return np.sqrt(((elem[0]-target[0])**2 + (elem[1]-target[1])**2)); 

def update2_domain(domain:np.ndarray.dtype):
    s = domain.shape;
    target = np.where(domain == 3);
    new_domain = deepcopy(domain)
    neighbours = [0,0,0,0,0,0,0,0];  
    for i in range(s[0]):
        for j in range(s[1]): 
            neighbours = np.array(get_neighbours(domain,(i,j)));
            distances = np.zeros((len(neighbours),1));
            # Is one of them the target.
            logical = neighbours == 3; 
            if(np.sum(logical)==1):
                continue; 
            else: 
                distances.append(distance_to_target((i,j),domain,tuple(target)));
            new_i = 
            new_domain[i][j] = 0; 
            new_domain[new_i][new_j] = 1;
    return new_domain; 

def update3_domain(domain:np.ndarray.dtype):
    return 