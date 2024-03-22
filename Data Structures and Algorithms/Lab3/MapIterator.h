#pragma once
#include "Map.h"
class MapIterator
{
	//DO NOT CHANGE THIS PART
	friend class Map;
private:
    const Map& map;
    int current;

    //moving the cursor to the next non-empty position
    void moveNext();

    MapIterator(const Map& m);
public:
	void first();
	void next();
	TElem getCurrent();
	bool valid() const;
};


