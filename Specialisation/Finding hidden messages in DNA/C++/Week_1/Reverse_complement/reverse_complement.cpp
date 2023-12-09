#include <map>
#include <string>
#include <string_view>
#include <fstream>
#include <iostream>
#include <algorithm>

std::string get_data(std::string& file_path) {
	std::fstream file;
	std::string data{ "" };
	file.open(file_path.c_str(), std::ios::in);
	if (file.is_open()) {
		std::string current_line;
		while (std::getline(file, current_line)) {
			data += current_line;
		}
		file.close();
	}

	return data;
}

std::string get_reverse_complement(const std::string& dna_strand) {
	const std::map<std::string, std::string> DNA_COMPLEMENT_MAP{ {"A", "T"}, {"G", "C"}, {"T", "A"}, {"C", "G"} };
	std::string complementary_strand{ "" };
	for (auto it = dna_strand.rbegin(); it != dna_strand.rend(); ++it) {
		std::string entry_string = std::string(1, *it);
		complementary_strand += DNA_COMPLEMENT_MAP.find(entry_string)->second;
	}
	return complementary_strand;
}
