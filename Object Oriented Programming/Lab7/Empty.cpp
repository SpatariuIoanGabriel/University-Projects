#include "Empty.h"
#include "Gopher.h"
#include "Plant.h"
#include "Fox.h"
#include "SimulationGrid.h"

std::string Empty::toString() const
{
	return "E";
}

Empty::Empty(int row1, int col1)
{
	this->row = row1;
	this->col = col1;
}


Entity* Empty::next(const SimulationGrid& g)
{
	int k1 = 0, k2 = 0, k3 = 0;
	for (int i = 0; i < g.getRows(); i++) {
		for (int j = 0; j < g.getCols(); j++) {
			if (g.grid[i][j]->what() == EntityType::GOPHER)
				k1++;
			if (g.grid[i][j]->what() == EntityType::FOX)
				k2++;
			if (g.grid[i][j]->what() == EntityType::PLANT)
				k3++;
		}
	}

	if (k1 > 1) {
		return new Gopher(row, col, 0);
	}
	else {
		if (k2 > 1) {
			return new Fox(row, col, 0);
		}
		else {
			if (k3 >= 1) {
				return new Plant(row, col);
			}
			else return new Empty(row, col);
		}
	}
}

std::ostream& operator<<(std::ostream& os, const Empty& empty) {
    os << empty.toString();
    return os;
}
