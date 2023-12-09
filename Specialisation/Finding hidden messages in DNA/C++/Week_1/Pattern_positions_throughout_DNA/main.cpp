#include <iostream>
#include "pattern_positions.h"

void main() {
	std::string path{ "C:\\Users\\nikik\\Desktop\\GitRepo\\Bioinformatics\\Specialisation\\Finding hidden messages in DNA\\C++\\Week_1\\Pattern_positions_throughout_DNA\\dataset.txt"};
	std::string_view pattern{"CTTGATCAT"};
	std::string data = get_data(path);
	std::string result = get_pattern_positions(data, pattern);
	std::cout << result;
}