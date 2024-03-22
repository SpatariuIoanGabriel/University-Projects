#pragma once
#include "SortedBag.h"

class SortedBag;
typedef int TComp;

class Stack {
private:
    BSTNode** elements;
    int topIndex;
    int capacity;

public:
    Stack();
    ~Stack();
    void push(BSTNode* element);
    void pop();
    BSTNode* top() const;
    bool empty() const;
    int getCapacity() const;
};


class SortedBagIterator {
    friend class SortedBag;

private:
    const SortedBag& sb;
    BSTNode* currentNode;
    Stack stack;
    SortedBagIterator(const SortedBag& sb);

public:
    TComp getCurrent();
    bool valid();
    void next();
    void first();
};
