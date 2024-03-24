#pragma once
#include "EntityType.h"
#include "SimulationGrid.h"
#include <string>
class Entity
{
public:
    ~Entity() = default;
	virtual EntityType what() = 0;
	virtual std::string toString() const;
	virtual Entity* next(const SimulationGrid& g) = 0;
    void demographics(unsigned int population[], const SimulationGrid& g);

protected:
	 int row{};
	 int col{}; // location of the life form
private:
};


