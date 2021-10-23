from grid import *

def test_grid():
    filename = "grid_pattern.dat";
    grid = DCSProblem(filename);
    grid.pprint();

def test_DCS_Problem(): 
    filename = "grid_pattern.dat"; 
    grid = DCSProblem(filename); 
    grid.pprint();
    grid.simulate(1); 
    print("")
    grid.pprint();

def main():
    # test_grid();
    test_DCS_Problem();

main();