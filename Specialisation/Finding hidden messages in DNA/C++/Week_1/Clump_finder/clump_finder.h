#include<string_view>
#include<string>
#include<vector>
#include<map>
#pragma once
#ifndef __COMMON_H__
#define __COMMON_H__
std::string get_data(std::string&);
std::vector<std::pair<std::string_view, size_t>> frequent_words(std::string_view, size_t);
std::vector<std::pair<std::string_view, size_t>> map_sort(const std::map<std::string_view, size_t>&);
bool cmp(std::pair<std::string_view, size_t>&, std::pair<std::string_view, size_t>&);
std::string clump_finder(std::string_view, size_t, size_t, size_t);
#endif