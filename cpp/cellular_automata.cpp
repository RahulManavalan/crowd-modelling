#include<iostream>
#include<cmath>
#include<unistd.h> 
#include<random> 

void print(bool* domain,const int dimx,const int dimy)
{
	for(int j=0;j<dimy;++j){
		for(int i=0;i<dimx;++i){
		std::cout << domain[i+j*dimx] << " "; 
		} 
		std::cout << std::endl; 
	}
} 

bool bool_rand()
{
	int seed = rand()%10; 
	std::mt19937 gen(seed);
	std::uniform_int_distribution<int> dist(0,10);
	if(dist(gen)<5){	
		return 1; 
	}
	else{
		return 0; 
	} 
}

bool* init_domain(const int& dimx,const int& dimy)
{
	bool* domain = new bool[dimx*dimy];
	for(int j=0;j<dimy;++j){
		for(int i=0;i<dimx;++i){
			domain[i+j*dimx] = bool_rand();
		} 
	}
	return domain;
} 

bool* automate(bool*& domain,const int& dimx,const int& dimy)
{
	int result; 
	bool* domain1 = new bool[dimx*dimy];
	for(int j=0;j<dimy;++j){
		for(int i=0;i<dimx;++i){
			result = domain[j*dimx+i] + domain[j*dimx-i] + domain[i*dimy+j] + domain[i*dimy-j];
			if(result<=3){
				domain1[i+j*dimx] = 1; 				
			} 
			else{
				domain1[i+j*dimx] = 0;
			} 
		} 
	} 
	delete[] domain;
	domain = NULL;
	return domain1;
}


int main(int argc,char** argv)
{
	int dimx,dimy,fill,nsteps; 
	if(argc>1){
		dimx = atoi(argv[1]); 
		dimy = atoi(argv[2]);
		nsteps = atoi(argv[3]);	
	}
	else{
		std::runtime_error("Insufficient number of arguments");
	} 
	auto domain = init_domain(dimx,dimy);

	for(int i=0;i<nsteps;++i){
		domain = automate(domain,dimx,dimy);
		print(domain,dimx,dimy);
		sleep(2); 
		system("clear");
	} 
}

/*
int main()
{
	std::cout << bool_rand() << std::endl; 
}
*/ 
