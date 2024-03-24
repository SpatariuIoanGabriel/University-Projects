
#define PUZZLE_H

#include<map>
#include<vector>
#include<string>
#include"Graph.h"
#include<fstream>
#include<istream>
#include<iostream>

class Puzzle
{
public:
	Puzzle(std::string fileName);
	bool stringsDifference(std::string word1, std::string word2);
	void generateGraph(int length);
	std::vector<std::string> getPath(std::string word1, std::string word2);

private:
	std::map<int, std::vector<std::string>> words;
	Graph<std::string, std::vector<std::string>> graph;
};
