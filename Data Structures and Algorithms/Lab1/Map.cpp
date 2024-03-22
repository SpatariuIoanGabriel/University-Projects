#include "Map.h"
#include "MapIterator.h"
#include <exception>
Map::Map() {
    this->e = new TElem[10];  // initial capacity of 10
    this->capacity = 10;
    this->length = 0;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

Map::~Map() {
    delete[] e;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

TValue Map::add(TKey c, TValue v) {
    // adds a pair (key,value) to the map
    //if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned
    //if the key does not exist, a new pair is added and the value null is returned
    if (this->length == this->capacity) {
        this->resize();  // double the capacity
    }

    for (int i = 0; i < this->length; i++) {
        if (this->e[i].first == c) {  // key already exists
            TValue old_val = this->e[i].second;
            this->e[i].second = v;
            return old_val;
        }
    }

    // key not found, add a new pair

    this->e[this->length] = std::make_pair(c, v);
    this->length++;
    return NULL_TVALUE;
}
//Best case θ(1), Worst case θ(n), Overall O(n)

TValue Map::search(TKey c) const {
    //searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TVALUE otherwise
    for (int i = 0; i < this->length; i++) {
        if (this->e[i].first == c) {
            return this->e[i].second;
        }
    }
    return NULL_TVALUE;  // key not found
}
//Best case θ(1), Worst case θ(n), Overall O(n)

TValue Map::remove(TKey c) {
    //removes a key from the map and returns the value associated with the key if the key existed ot null: NULL_TVALUE otherwise
    for (int i = 0; i < this->length; i++) {
        if (this->e[i].first == c) {
            TValue old_val = this->e[i].second;
            // move the last pair to the current position
            this->e[i] = this->e[this->length-1];
            this->length--;
            return old_val;
        }
    }
    return NULL_TVALUE;  // key not found
}
//Best case θ(1), Worst case θ(n), Overall O(n)

int Map::size() const {
    //returns the number of pairs (key,value) from the map
    return this->length;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

bool Map::isEmpty() const {
    return this->length == 0;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

void Map::resize() {
//    double capacity
    this->capacity *= 2;
    // allocate a new array
    TElem* new_e = new TElem[this->capacity];
//    copy all the elements
    for (int i = 0; i < this->length; i++) {
        new_e[i] = this->e[i];
    }
//    release memory
    delete[] this->e;
//    we make the field w to refer the new array
    this->e = new_e;
}
//Best case θ(n), Worst case θ(n), Overall 0(n)

MapIterator Map::iterator() const {
    return MapIterator(*this);
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

MapIterator::MapIterator(const Map& m) : map(m) {
    this->current = 0;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

void MapIterator::first() {
    this->current = 0;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

void MapIterator::next() {
    if(!valid()){
        throw std::exception();
    } else
        this->current++;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

TElem MapIterator::getCurrent() {
    if(!valid())
        throw std::exception();
    else
        return this->map.e[this->current];
}
//Best case θ(1), Worst case θ(1), Overall θ(1)

bool MapIterator::valid() const {
    return this->current >= 0 && this->current < this->map.length;
}
//Best case θ(1), Worst case θ(1), Overall θ(1)
