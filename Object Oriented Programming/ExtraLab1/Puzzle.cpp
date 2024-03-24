#include "Puzzle.h"
#include<istream>


Puzzle::Puzzle(std::string fileName)
{
	std::ifstream f_cin(fileName);
	std::string line;
	while (getline(f_cin, line))
	{
		int length = line.size();
		std::string word = line.substr(0, length - 1);
		words[length - 1].push_back(word);
	}
}

bool Puzzle::stringsDifference(std::string word1, std::string word2)
{
	if (word1.size() != word2.size())
		return false;
	else
	{
		int found = 0;
		for (int i = 0; i < word1.size(); i++)
		{
			if (word1[i] != word2[i])
			{
				found++;
			}
			if (found > 1)
			{
				return false;
			}
		}
		return found == 1;
	}
}

void Puzzle::generateGraph(int length)
{
	for (const auto& word1 : words[length])
	{
		for (const auto& word2 : words[length])
		{
			if (stringsDifference(word1, word2))
			{
				graph.addEdge(word1, word2);
			}
		}

	}
}

std::vector<std::string> Puzzle::getPath(std::string word1, std::string word2)
{
	return graph.bfs(word1, word2);
}
