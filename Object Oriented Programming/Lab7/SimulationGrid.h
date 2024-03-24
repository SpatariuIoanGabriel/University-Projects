#pragma once
#define MAX_ROWS 100
#define MAX_COLS 100
#include <iostream>
// forward class declaration for Entity
class Entity;
class SimulationGrid
{
public:
	int getRows() const;
	int getCols() const;

	void setRows(int x);
	void setCols(int y);

	friend class Entity;
	friend class Empty;
    friend class Plant;
	friend std::ostream& operator<<(std::ostream& out, const SimulationGrid& m);
    Entity* grid[MAX_ROWS][MAX_COLS];

private:
	int rows;
	int cols;


};
