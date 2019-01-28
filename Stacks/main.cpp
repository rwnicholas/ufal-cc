#include <iostream>

char valor(){
	return ')';
}

int main(int argc, char *argv[]){
	if (valor == ')'){
		std::cout << "Ok" << std::endl;
	} else {
		std::cout << "Deu ruim" << std::endl;
	}
	return 0;
}