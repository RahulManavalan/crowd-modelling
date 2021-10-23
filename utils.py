from os import closerange
import numpy as np
import re
import matplotlib.pyplot as plt
from type import Type

def parse_elem(elem:str)->int:     
    if(elem=='e'): 
        return 0;
    elif(elem=='t'): 
        return 3
    elif(elem=='p'): 
        return 1;
    elif(elem=='o'): 
        return 2; 
    else: 
        raise ValueError("Unsupported element in the input file");

def parse_file(filename:str)->np.ndarray.dtype: 
    file = open(filename);
    lines = file.readlines(); 
    dim = len(lines); 
    array = np.zeros((dim,dim)); 
    for i,line in enumerate(lines):
        if(line[0]=='#'):
            continue; 
        row = re.split(" |\n",line);
        row.pop(-1);
        for j,elem in enumerate(row):  
            array[i,j] = parse_elem(elem);
    return array;

def find_neighbour(i:int,j:int,xmax:int,ymax:int):
    neighbour = [];
    if(i==0 and j==0): 
        neighbour += [(i,j+1),(i+1,j+1),(i+1,j)];
    elif(i==xmax-1 and j==0): 
        neighbour+=[(i,j+1),(i-1,j),(i-1,j+1)];
    elif(i==0 and j==ymax-1): 
        neighbour+=[(i+1,j),(i+1,j-1),(i,j-1)];
    elif(i==xmax-1 and j==ymax-1):
        neighbour+=[(i,j-1),(i-1,j-1),(i-1,j)];
    elif(i==0): 
        neighbour+=[(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1)];
    elif(i==xmax-1): 
        neighbour+=[(i,j+1),(i,j-1),(i-1,j-1),(i-1,j),(i-1,j+1)];
    elif(j==0):
        neighbour+=[(i,j+1),(i+1,j+1),(i+1,j),(i-1,j),(i-1,j+1)]; 
    elif(j==ymax-1):
        neighbour+=[(i+1,j),(i+1,j-1),(i,j-1),(i-1,j-1),(i-1,j)]; 
    else: 
        neighbour+=[(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1),(i-1,j-1),(i-1,j),(i-1,j+1)];  
    return neighbour

def find_state(char:np.float64): 
    if(char==0):
        return Type.Empty;
    elif(char==1): 
        return Type.Pedestrian; 
    elif(char==2): 
        return Type.Obstacle;
    elif(char==3):
        return Type.Target;
    else:  
        RuntimeError("Invalid character used in __find_state__");

def visualize(grid:np.ndarray.dtype):
    dims = grid.shape; 
    xlim = dims[0]; ylim = dims[1];  
    X = grid;
    fig, ax = plt.subplots()
    ax.imshow(X, interpolation='nearest')
    numrows, numcols = X.shape
    def format_coord(x, y):
        col = int(x);
        row = int(y);
        if col >= 1 and col < numcols and row >= 1 and row < numrows:
            z = X[row, col]
            return 'x=%1.4f, y=%1.4f, z=%1.4f' % (x, y, z)
        else:
            return 'x=%1.4f, y=%1.4f' % (x, y)
    plt.xlim([0,xlim]); 
    plt.ylim([0,ylim]);
    ax = plt.gca();
    ax.format_coord = format_coord 
    ax.axes.xaxis.set_ticklabels([]); 
    ax.axes.yaxis.set_ticklabels([]);
    plt.grid();
    plt.show(); 