#include<fstream>
#include<iostream>
#include<string>

/*First we use a function to retrieve the data as a string from the  file.*/

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

/*Then we do the pattern matching by implementing a rolling window function, which checks if the next characters
match our pattern.*/

int pattern_matching(std::string_view data, std::string_view pattern) {
	//Apply a rolling window function. Until we run out of string, check if the pattern matches the next characters.
	//param data: The whole string that will be used to match the pattern against.
	//param pattern: The string that will be searched for in the data string.
	//return: Count of occurrences of such pattern in the string.
	int result_count{ 0 };
	size_t data_length = data.length();
	size_t pattern_length = pattern.length();
	size_t current_index{ 0 };

	while (current_index <= (data_length - pattern_length)) {
		std::string_view potential_match = data.substr(current_index, pattern_length);
		if (potential_match == pattern) {
			++result_count;
		}
		++current_index;
	}
	return result_count;
}