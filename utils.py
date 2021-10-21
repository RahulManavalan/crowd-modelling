from os import closerange
import numpy as np
import re
import matplotlib.pyplot as plt

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

def parse_tensor_file(filename:str):
    return 

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