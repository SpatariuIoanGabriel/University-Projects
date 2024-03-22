#include "Map.h"
#include "MapIterator.h"
#include <stdexcept>

using namespace std;

MapIterator::MapIterator(const Map& m) : map(m) {
    current = 0;
    moveNext();
}
//Best case θ(1), Worst case 0(n), Overall O(n)

void MapIterator::first() {
    current = 0; // Start before the first valid element
    moveNext();
}
//Best case θ(1), Worst case 0(n), Overall O(n)

void MapIterator::next() {
    if (!valid()) {
        throw std::exception();
    }
    current++;
    moveNext();
}
//Best case θ(1), Worst case 0(n), Overall O(n)

TElem MapIterator::getCurrent() {
    if (!valid()) {
        throw std::exception(); // Throw an exception if the iterator is not valid
    }

    return map.e[current]; // Return the element at the current position
}
//Best case θ(1), Worst case 0(1), Overall 0(1)

bool MapIterator::valid() const {
    return current < map.m;
}
//Best case θ(1), Worst case 0(1), Overall 0(1)

void MapIterator::moveNext() {
    while ((current < map.m) && (map.e[current].first == NULL_TVALUE)) {
        current++;
    }
}
//Best case θ(1), Worst case 0(n), Overall O(n)