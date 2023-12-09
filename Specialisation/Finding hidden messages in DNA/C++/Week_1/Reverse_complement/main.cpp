#include<iostream>
#include<string_view>
#include "reverse_complement.h"

void main() {
	std::string path{ "C:\\Users\\nikik\\Desktop\\GitRepo\\Bioinformatics\\Specialisation\\Finding hidden messages in DNA\\C++\\Week_1\\Reverse_complement\\dataset.txt" };
	std::string dna_strand = get_data(path);
	std::string reverse_complement = get_reverse_complement(dna_strand);
	std::cout << reverse_complement;
}