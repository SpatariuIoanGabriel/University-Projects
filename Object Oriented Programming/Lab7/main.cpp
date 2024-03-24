#include <iostream>
#include "Entity.h"
#include "EntityType.h"
#include "SimulationGridTest.h"
#include "PlantTest.h"
#include "EmptyTest.h"

int main(){
    testSimulationGrid();
    testPlant();
    testEmpty();
    std::cout << "All Simulation Grid Tests passed!" << std::endl;
    std::cout << "All Plant Tests passed!" << std::endl;
    std::cout << "All Empty Tests passed!" << std::endl;
    return 0;
}
