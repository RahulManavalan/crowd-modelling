#include<vector>
#include<iostream> 
#include<immintrin.h> 
#include<omp.h>

#define NUM_THREADS 8

enum state
{
	source, 
	target, 
	inter,
	obstacle
};

void print(state* ptr,const int dimx,const int dimy)
{
	state s;
	for(int i=0;i<dimx;i++){
		for(int j=0;j<dimy;++j){
			s = ptr[i+j*dimx];
			switch(s)	
			{
			case state::source:
				std::cout << "\xF0\x9F\x9A\xA9";  
				break;
			case state::target: 
				std::cout << "\xF0\x9F\x8F\x81"; 
				break; 
			case state::inter: 
				std::cout << "\xE2\x96\xAB";
				break;
			case state::obstacle: 
				std::cout << "\xE2\x96\xAA";
				break;  
			default: 
				std::runtime_error("Invalid state.");
				break;
			} 
			std::cout << "  ";
		} 
		std::cout << std::endl; 
	}
}

// How can I vectorize this ? 
inline void fill(state* ptr,const int& n)
{	
	#pragma omp parallel for schedule(dynamic,8) 
	for(int i=0;i<n;++i){
		ptr[i] = state::inter; 
	}	 
} 

// Stores the elements in a linear vector in column major ordering.
state* build_board(const int dimx,const int dimy)
{
	int n = dimx*dimy; 
	state* board = new state[n];
	fill(board,n);
	return board; 
} 

inline void set_element(state* board,const int &idx,const int &idy,const int& dimx,const state& s)
{
	board[idx+idy*dimx] = s; 
} 
 
int main(int argc,char** argv) 
{
	int dimx,dimy;
	if(argc>1){
		dimx = atoi(argv[1]); 
		dimy = atoi(argv[2]); 
	}
	state*  board = build_board(dimx,dimy); 
	set_element(board,0,0,dimx,state::source);
	set_element(board,dimx-1,dimy-1,dimx,state::target);
	print(board,dimx,dimy); 	
	delete[] board; 
}
