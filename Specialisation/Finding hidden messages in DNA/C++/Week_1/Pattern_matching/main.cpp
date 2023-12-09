#include <iostream>
#include <string>
#include "Pattern_matching.h"

void main() {
	std::string path{ "C:\\Users\\nikik\\Desktop\\GitRepo\\Bioinformatics\\Specialisation\\Finding hidden messages in DNA\\C++\\Week_1\\Pattern_matching\\dataset.txt" };
	std::string_view to_match{ "GTCCAGTGT" };
	std::string data = get_data(path);
	data = std::string_view(data);
	int result = pattern_matching(data, to_match);
	std::cout << result << std::endl;
}