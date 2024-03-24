#include "SimulationGrid.h"

std::ostream& operator<<(std::ostream& out, const SimulationGrid& m)
{
	for (int i = 0; i < m.rows; i++)
	{
		for (int j = 0; j < m.cols; j++) {
			out << m.grid[i][j] << " ";
		}
		out << std::endl;
	}
	return out;
}

int SimulationGrid::getRows() const
{
	return rows;
}

int SimulationGrid::getCols() const
{
	return cols;
}

void SimulationGrid::setRows(int x)
{
	rows = x;
}

void SimulationGrid::setCols(int y)
{
	cols = y;
}
