#include "Plant.h"
#include "Empty.h"
#include "Gopher.h"
#include "SimulationGrid.h"
#include <cassert>

void testPlant() {
    // Test constructor and toString
    Plant p(2, 3);
    assert(p.toString() == "P");

    // Test next for a case where no gophers are nearby
    SimulationGrid g1{};
    g1.grid[1][1] = new Plant(1, 1);
    g1.grid[1][2] = new Plant(1, 2);
    g1.grid[2][1] = new Plant(2, 1);
    g1.grid[2][2] = new Plant(2, 2);
    g1.grid[3][3] = new Empty(3, 3);
    Entity* result1 = p.next(g1);
    assert(result1->what() == EntityType::PLANT);

    // Test next for a case where there are 3 gophers nearby
    SimulationGrid g3{};
    g3.grid[1][1] = new Gopher(1, 1, 0);
    g3.grid[1][2] = new Gopher(1, 2, 0);
    g3.grid[2][1] = new Gopher(2, 1, 0);
    Entity* result3 = p.next(g3);
    assert(result3->what() == EntityType::PLANT);

    // Test next for a case where there are 4 plants and 3 gophers nearby
    SimulationGrid g4{};
    g4.grid[1][1] = new Plant(1, 1);
    g4.grid[1][2] = new Plant(1, 2);
    g4.grid[2][1] = new Plant(2, 1);
    g4.grid[2][2] = new Plant(2, 2);
    g4.grid[3][3] = new Gopher(3, 3, 0);
    g4.grid[3][4] = new Gopher(3, 4, 0);
    g4.grid[4][3] = new Gopher(4, 3, 0);
    Entity* result4 = p.next(g4);
    assert(result4->what() == EntityType::PLANT);

}
