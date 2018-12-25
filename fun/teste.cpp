#include <iostream>

int fib(int m){
	int F = 0;
	int ant = 0;

	for(int i = 1; i <= m; i++){
		if (i == 1){
			F = 1;
			ant = 0;
		} else {
			F += ant;
			ant = F - ant % (1000000007);
		}
	}
	return F;
}

int main(int argc, char *argv[]){
	int val;
	std::cin >> val;
	std::cout << fib(val) << std::endl;
	return 0;
}