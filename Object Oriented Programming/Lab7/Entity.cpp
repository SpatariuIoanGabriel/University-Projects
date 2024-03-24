#include "Entity.h"
#include "EntityType.h"
#include <algorithm> // for std::fill

std::string Entity::toString() const
{
	return "Entity";
}


void Entity::demographics(unsigned int population[], const SimulationGrid& g)
{
	// return number of life form for each life form

	std::fill(population, population + 4, 0);
	// offsets for the neighbors' coordinates
	int dx[]{ 0, 0, 1, 1, 1, -1, -1, -1 };
	int dy[]{ 1, -1, -1, 0, 1,  -1, 0, 1 };
	// row : row+1, row-1
	// col: col+0, col+0
	unsigned int numNeigh{ sizeof(dy) / sizeof(dy[0]) };

	for (unsigned int i{ 0 }; i < numNeigh; ++i) {
		int r{ row + dy[i] };
		int c{ col + dx[i] };
		if ((r >= 0 && r <= 3 && c >= 0 && c <= 3)) {
			EntityType et = g.grid[r][c]->what();
			population[to_underlying(et)]++;
		}
	}
}

Entity* Entity::next(const SimulationGrid& g)
{
    return nullptr;
}

