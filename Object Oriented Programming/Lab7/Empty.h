#pragma once
#include "Entity.h"
#include "SimulationGrid.h"
class Empty : public Entity{

public:
	std::string toString() const override;
	Empty(int row1, int col1);
    EntityType what() override { return EntityType::EMPTY; }
	Entity* next(const SimulationGrid& g) override;

    friend std::ostream& operator<<(std::ostream& os, const Empty& empty);
};