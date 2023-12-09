#include<string>
#include<iostream>
#include "clump_finder.h"

void main() {
	std::string path{"C:\\Users\\nikik\\Desktop\\GitRepo\\Bioinformatics\\Specialisation\\Finding hidden messages in DNA\\C++\\Week_1\\Clump_finder\\dataset.txt"};
	size_t k_mer_length{9};
	size_t dna_range{500};
	size_t k_mer_amount{3};
	std::string data = get_data(path);
	std::string result = clump_finder(data, k_mer_length, dna_range, k_mer_amount);
	std::cout << result;
}