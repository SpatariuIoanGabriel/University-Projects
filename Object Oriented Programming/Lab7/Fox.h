#pragma once
#include "Entity.h"
#include "Animal.h"
class Fox : public Animal {

public:
	std::string toString() const override;
	Fox(int row1, int col1, int i);
	friend class Entity;
	EntityType what() override { return EntityType::FOX; }
	Entity* next(const SimulationGrid& g) override;

    friend std::ostream& operator<<(std::ostream& os, const Fox& fox);
};