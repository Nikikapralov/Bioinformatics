#include "frequent_words.h"
#include "iostream"

void main() {

	std::string path{ "C:\\Users\\nikik\\Desktop\\GitRepo\\Bioinformatics\\Specialisation\\Finding hidden messages in DNA\\C++\\Week_1\\Frequent_words\\dataset.txt"};
	std::string data = get_data(path);
	size_t k_mer_size{ 13 };
	std::string result = frequent_words(data, k_mer_size);
	std::cout << result;
}