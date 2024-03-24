#include "Fox.h"
#include "Empty.h"

std::string Fox::toString() const
{
	return "F";
}

Fox::Fox(int row1, int col1, int i)
{
	this->row = row1;
	this->col = col1;
}

Entity* Fox::next(const SimulationGrid& g)
{
    // Initialize variables to keep track of the number of gophers in the neighborhood
    int numGophers = 0;

    // Iterate over the neighbors of the current fox and count the number of gophers
    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            if (dx == 0 && dy == 0) continue; // Skip the current cell

            int row = this->row + dy;
            int col = this->col + dx;

            if (row < 0 || row >= 4 || col < 0 || col >= 4) continue; 

            EntityType neighborType = g.grid[row][col]->what();
            if (neighborType == EntityType::GOPHER) numGophers++;
        }
    }

    // Check the conditions for the next iteration
    if (this->age >= 5 || numGophers == 0) {
        return new Empty(this->row, this->col);
    } else {
        return new Fox(this->row, this->col, this->age + 1);
    }
}

std::ostream& operator<<(std::ostream& os, const Fox& fox) {
    os << fox.toString();
    return os;
}
