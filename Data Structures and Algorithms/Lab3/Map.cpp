#include <utility>
#include "Map.h"
#include "MapIterator.h"
#include <functional>

using namespace std;

// i is the probe number
int Map::h(TKey key, int i) const {
    const int h1 = std::hash<TKey>{}(key) % m;  // Simple hash function applied to the key.
    // % m operation ensures that the hash value remains within the range of the map
    return (h1 + i + i * i) % m;
    //adds the probe number (i) multiplied by the quadratic probing
}
//Best case θ(1), Worst case 0(1), Overall 0(1)

Map::Map() {
    m = MAX;
    for (int i = 0; i < m; i++) {
        e[i] = NULL_TELEM;
    }
}
//Best case θ(1), Worst case 0(1), Overall 0(1)

Map::~Map() {
}

// adds a pair (key,value) to the map
//if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned
//if the key does not exist, a new pair is added and the value null is returned
TValue Map::add(TKey c, TValue v) {
    int i = 0; // probe number
    bool found = false;
    TValue oldValue = NULL_TVALUE;

    do {
        int j = h(c, i); // calculate the hash value
        if (e[j].first == NULL_TVALUE) {
            // Add a new element
            oldValue = NULL_TVALUE;
            e[j].first = c;
            e[j].second = v;
            found = true;
        }
        else if (e[j].first == c) {
            // Update the existing element
            oldValue = e[j].second;
            e[j].second = v;
            found = true;
        }
        i++;
    } while (i < m && !found);

    return oldValue;
}
//Best case θ(1), Worst case 0(n), Overall O(n)


//removes a key from the map and returns the value associated with the key if the key existed ot null: NULL_TVALUE otherwise
TValue Map::remove(TKey key) {
    int i = 0;
    int j = h(key, i);

    while (i < m && e[j] != NULL_TELEM) {
        if (e[j].first == key) {
            TValue oldValue = e[j].second;
            e[j] = NULL_TELEM;
            //rehash
            int k = j;
            while (e[k] != NULL_TELEM) {
                i++;
                k = h(key, i);
                if (e[k] != NULL_TELEM && h(e[k].first, 0) != j) {
                    e[j] = e[k];
                    e[k] = NULL_TELEM;
                    j = k;
                }
            }
            return oldValue;
        }
    }

    return NULL_TVALUE;
}
//Best case θ(1), Worst case 0(n), Overall O(n)


//searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TVALUE otherwise
TValue Map::search(TKey c) const {
    int i = 0; // probe number

    do {
        int j = h(c, i);
        if (e[j] == NULL_TELEM) {
            return NULL_TVALUE;
        }
        else if (e[j].first == c) {
            return e[j].second;
        }
        i++;
    } while (i < m);

    return NULL_TVALUE;
}
//Best case θ(1), Worst case 0(n), Overall O(n)

// returns the number of pairs (key, value) in the map
int Map::size() const {
    int count = 0;
    for (int i = 0; i < m; i++) {
        if (e[i] != NULL_TELEM) {
            count++;
        }
    }
    return count;
}
//Best case θ(1), Worst case 0(n), Overall O(n)


bool Map::isEmpty() const {
    return size() == 0;
}
//Best case θ(1), Worst case 0(1), Overall 0(1)

MapIterator Map::iterator() const {
    return MapIterator(*this);
}
//Best case θ(1), Worst case 0(1), Overall 0(1)