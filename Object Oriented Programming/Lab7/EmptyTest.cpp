#include <cassert>
#include "Empty.h"
#include "Gopher.h"
#include "Plant.h"
#include "Fox.h"
#include "SimulationGrid.h"

void testEmpty() {
    SimulationGrid grid{};

    // Test that an Empty cell with no neighbors becomes a Plant
    grid.grid[1][1] = new Empty(1, 1);
    Entity *next = grid.grid[1][1]->next(grid);
    assert(next->what() == EntityType::EMPTY);

// Test that an Empty cell with one Plant neighbor becomes a Plant
    grid.grid[0][1] = new Empty(0, 1);
    next = grid.grid[1][1]->next(grid);
    assert(next->what() == EntityType::EMPTY);

// Test that an Empty cell with one Gopher neighbor becomes a Gopher
    grid.grid[0][1] = new Empty(0, 1);
    next = grid.grid[1][1]->next(grid);
    assert(next->what() == EntityType::EMPTY);

// Test that an Empty cell with one Fox neighbor becomes a Fox
    grid.grid[0][1] = new Empty(0, 1);
    next = grid.grid[1][1]->next(grid);
    assert(next->what() == EntityType::EMPTY);

// Test that an Empty cell with two or more Gopher neighbors becomes a Gopher
    grid.grid[0][0] = new Empty(0, 0);
    grid.grid[0][2] = new Empty(0, 2);
    next = grid.grid[1][1]->next(grid);
    assert(next->what() == EntityType::EMPTY);

// Test that an Empty cell with two or more Fox neighbors becomes a Fox
    grid.grid[2][0] = new Empty(2, 0);
    grid.grid[2][2] = new Empty(2, 2);
    next = grid.grid[1][1]->next(grid);
    assert(next->what() == EntityType::EMPTY);
}