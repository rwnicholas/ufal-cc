#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>

boost::multiprecision::cpp_int fib(int m){
	boost::multiprecision::cpp_int F = 0;
	boost::multiprecision::cpp_int ant = 0;

	for(int i = 1; i <= m; i++){
		if (i == 1){
			F = 1;
			ant = 0;
		} else {
			F += ant;
			ant = (F - ant) % (1000000007);
		}
	}
	return F;
}

int main(int argc, char *argv[]){
	std::cout << fib(100000000) << std::endl;
	return 0;
}