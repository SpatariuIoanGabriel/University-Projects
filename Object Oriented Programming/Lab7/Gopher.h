#pragma once
#include "Entity.h"
#include "Animal.h"
class Gopher : public Animal {

public:
	std::string toString() const override;
	Gopher(int row1, int col1, int i);
	EntityType what() override { return EntityType::GOPHER; }
	Entity* next(const SimulationGrid& g) override;

    friend std::ostream& operator<<(std::ostream& os, const Gopher& gopher);
};