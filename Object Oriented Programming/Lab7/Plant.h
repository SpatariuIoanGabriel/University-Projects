#pragma once
#include "Entity.h"

class Plant : public Entity {

public:
    std::string toString() const override;
    Plant(int row1, int col1);
    EntityType what() override { return EntityType::PLANT; }
    Entity* next(const SimulationGrid& g) override;

    friend std::ostream& operator<<(std::ostream& os, const Plant& plant);
};
