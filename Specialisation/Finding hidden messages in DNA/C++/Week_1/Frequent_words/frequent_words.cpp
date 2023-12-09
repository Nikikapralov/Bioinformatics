#include<fstream>
#include<iostream>
#include<string>
#include<vector>
#include<string>
#include<string_view>
#include<map>
#include<algorithm>

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

// Comparator function to sort pairs 
// according to second value 
bool cmp(std::pair<std::string_view, size_t>& a, std::pair<std::string_view, size_t>& b)
{
	return a.second > b.second;
}

// Function to sort the map according 
// to value in a (key-value) pairs 
std::vector<std::pair<std::string_view, size_t>> map_sort(std::map<const std::string_view, size_t>& Map)
{

	// Declare vector of pairs 
	std::vector<std::pair<std::string_view, size_t>> sorted;

	// Copy key-value pair from Map 
	// to vector of pairs 
	for (auto& it : Map) {
		sorted.push_back(it);
	}

	// Sort using comparator function 
	std:sort(sorted.begin(), sorted.end(), cmp);
	return sorted;
}

std::string extract_result(std::vector<std::pair<std::string_view, size_t>> sorted) {
	//Extract the result from the sorted pairs. Only the ones with the highest result are needed.
	//param sorted: A vector holding sorted pairs of k-mer and its count in the data.
	//return: A string with the keys of those k-mers with highest count.
	size_t highest_count = sorted[0].second;
	std::string result_string { "" };

	for (auto& current_pair: sorted) {
		if (current_pair.second == highest_count){
			result_string += current_pair.first;
			result_string += " ";
			continue;
		}
		return result_string;
	}
}

std::string frequent_words(std::string_view data, size_t k_mer_size) {
	//Use a map so that one pass of the data is enough and time complexity is O(n) isntead of O(n**2)
	//param data: The data that is to be checked for the most frequent k-mers.
	//param k_mer_size: The size of the k-mers that are to be searched for.
	//return: String result with the most frequent k-mers of size k-mer-size in the data.
	std::map<const std::string_view, size_t> k_mer_count_map{};
	size_t current_index{ 0 };
	size_t maximal_index = data.length() - k_mer_size;
	while (current_index <= maximal_index) {
		std::string_view k_mer = data.substr(current_index, k_mer_size);
		++k_mer_count_map[k_mer];
		++current_index;
	}
	std::vector<std::pair<std::string_view, size_t>> sorted = map_sort(k_mer_count_map);
	std::string final_result = extract_result(sorted);
	return final_result;
}