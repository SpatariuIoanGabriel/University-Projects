#include "SimulationGrid.h"
#include "Empty.h"
#include "Plant.h"
#include <cassert>
#include <sstream>

void testSimulationGrid() {
    SimulationGrid grid{};

    // Test initial rows and cols
    assert(grid.getRows() == 0);
    assert(grid.getCols() == 0);

    // Test set rows and cols
    grid.setRows(5);
    grid.setCols(10);
    assert(grid.getRows() == 5);
    assert(grid.getCols() == 10);

    // Test adding entities
    Entity* empty = new Empty(2, 2);
    Entity* plant = new Plant(1, 1);
    grid.grid[2][2] = empty;
    grid.grid[1][1] = plant;
    assert(grid.grid[2][2] == empty);
    assert(grid.grid[1][1] == plant);

    // Test output stream
    std::ostringstream oss;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 10; j++) {
            if (grid.grid[i][j] == nullptr) {
                oss << "E ";
            } else if (grid.grid[i][j]->what() == EntityType::PLANT) {
                oss << "P ";
            } else if (grid.grid[i][j]->what() == EntityType::GOPHER) {
                oss << "G ";
            } else {
                oss << "E ";
            }
        }
        oss << "\n";
    }
    std::string expectedOutput =
            "E E E E E E E E E E \n"
            "E P E E E E E E E E \n"
            "E E E E E E E E E E \n"
            "E E E E E E E E E E \n"
            "E E E E E E E E E E \n";
    assert(oss.str() == expectedOutput);


    // Test invalid row and col
    assert(grid.grid[5][5] == nullptr);
    assert(grid.grid[2][10] == nullptr);

}
