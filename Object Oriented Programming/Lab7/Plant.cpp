#include "Plant.h"
#include "Empty.h"
#include "Gopher.h"

std::string Plant::toString() const
{
	return "P";
}

Plant::Plant(int row1, int col1)
{
	this->row = row1;
	this->col = col1;
}

Entity* Plant::next(const SimulationGrid& g)
{   int gopherCount = 0;
    int plantCount = 0;
    // count the number of gophers and plants in the neighborhood
    for (int i = row - 1; i <= row + 1; i++) {
        for (int j = col - 1; j <= col + 1; j++) {
            // skip out of bounds cells
            if (i < 0 || i >= g.getRows() || j < 0 || j >= g.getCols()) {
                continue;
            }
            if (g.grid[i][j]->what() == EntityType::GOPHER) {
                gopherCount++;
            }
            else if (g.grid[i][j]->what() == EntityType::PLANT) {
                plantCount++;
            }
        }
    }

    if (gopherCount > (2 * plantCount)) {
        return new Empty(row, col);
    }
    else if (gopherCount >= 3) {
        return new Gopher(row, col, 0);
    }
    else {
        return new Plant(row, col);
    }

}

std::ostream& operator<<(std::ostream& os, const Plant& plant) {
    os << plant.toString();
    return os;
}
