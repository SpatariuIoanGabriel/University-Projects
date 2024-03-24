#include "Plant.h"
#include "Empty.h"
#include "Gopher.h"
#include "Fox.h"

std::string Gopher::toString() const
{
	return "G";
}

Gopher::Gopher(int row1, int col1, int i)
{
	this->row = row1;
	this->col = col1;
}

Entity* Gopher::next(const SimulationGrid& g)
{
    // Initialize variables to keep track of the number of plants, foxes, and gophers in the neighborhood
    int numPlants = 0;
    int numFoxes = 0;
    int numGophers = 0;

    // Iterate over the neighbors of the current gopher and count the number of plants, foxes, and gophers
    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            if (dx == 0 && dy == 0) continue; // Skip the current cell

            int row = this->row + dy;
            int col = this->col + dx;

            if (row < 0 || row >= 4 || col < 0 || col >= 4) continue; // Skip cells outside of the grid

            EntityType neighborType = g.grid[row][col]->what();
            if (neighborType == EntityType::PLANT) numPlants++;
            else if (neighborType == EntityType::FOX) numFoxes++;
            else if (neighborType == EntityType::GOPHER) numGophers++;
        }
    }

    // Check the conditions for the next iteration
    if (this->age == 4 || numPlants == 0) {
        return new Empty(this->row, this->col);
    } else if (numFoxes >= numGophers) {
        return new Fox(this->row, this->col, 0);
    } else {
        return new Gopher(this->row, this->col, this->age + 1);
    }
}

std::ostream& operator<<(std::ostream& os, const Gopher& gopher) {
    os << gopher.toString();
    return os;
}

