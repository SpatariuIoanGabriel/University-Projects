#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;

MapIterator::MapIterator(const Map& d) : map(d)
{
    current = 0;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

void MapIterator::first() {
    current = 0;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

void MapIterator::next() {
    if (!valid()) {
        throw exception();
    }
    current++;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

TElem MapIterator::getCurrent(){
    if (!valid()) {
        throw exception();
    }
    return map.e[current];
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

bool MapIterator::valid() const {
    return current >= 0 && current < map.length;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)
