#include <string>
#include <string_view>
#include <iostream>
#include <fstream>

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

std::string get_pattern_positions(std::string_view data, std::string_view pattern) {
	std::string final_results{""};
	size_t current_index{ 0 };
	size_t pattern_length = pattern.length();
	size_t maximal_index = data.length() - pattern_length;

	while (current_index <= maximal_index) {
		std::string_view potential_match = data.substr(current_index, pattern_length);
		if (potential_match == pattern) {
			final_results += std::to_string(current_index);
			final_results += " ";
		}
		++current_index;
	}
	return final_results;
}
