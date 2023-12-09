#include<string_view>
#include<string>
#include<vector>
#include<map>
#pragma once
#ifndef __COMMON_H__
#define __COMMON_H__
std::string get_data(std::string&);
std::string frequent_words(std::string_view, size_t);
std::vector<std::pair<std::string_view, size_t>> map_sort(const std::map<std::string_view, size_t>&);
bool cmp(std::pair<std::string_view, size_t>&, std::pair<std::string_view, size_t>&);
#endif