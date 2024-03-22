#include <exception>
#include "ListIterator.h"
#include "IteratedList.h"

IteratedList::IteratedList() {
    length = 0;
    head = -1;
    tail = -1;
    firstEmpty = 0;
    for (int i = 0; i < cp - 1; i++) {
        next[i] = i + 1;
        prev[i + 1] = i;
    }
    next[cp - 1] = -1;
}

int IteratedList::size() const {
    return length;
}

bool IteratedList::isEmpty() const {
    return length == 0;
}

ListIterator IteratedList::first() const {
    return ListIterator(*this);
}

TElem IteratedList::getElement(ListIterator pos) const {
    if (!pos.valid()) {
        throw std::exception();
    }
    return elements[pos.current];
}

TElem IteratedList::remove(ListIterator& pos) {
    if (!pos.valid()) {
        throw std::exception();
    }
    int current = pos.current;
    int prevElem = prev[current];
    int nextElem = next[current];
    if (prevElem == -1) {
        head = nextElem;
    }
    else {
        next[prevElem] = nextElem;
    }
    if (nextElem == -1) {
        tail = prevElem;
    }
    else {
        prev[nextElem] = prevElem;
    }
    TElem removedElem = elements[current];
    deallocate(current);
    length--;
    pos.current = nextElem;
    return removedElem;
}

ListIterator IteratedList::search(TElem e) const {
    ListIterator current = first();
    while (current.valid()) {
        if (getElement(current) == e) {
            return current;
        }
        current.next();
    }
    return current;
}


TElem IteratedList::setElement(ListIterator pos, TElem e) {
    if (!pos.valid()) {
        throw std::exception();
    }
    int current = pos.current;
    TElem oldValue = elements[current];
    elements[current] = e;
    return oldValue;
}

void IteratedList::addToBeginning(TElem e) {
    int newPosition = allocate();

    elements[newPosition] = e;
    next[newPosition] = head;
    prev[newPosition] = -1;
    prev[head] = newPosition;

    if (isEmpty()) {
        tail = newPosition;
    }

    head = newPosition;
    length++;
}

void IteratedList::addToPosition(ListIterator& pos, TElem e) {
    if (!pos.valid()) {
        throw std::exception();
    }
    int current = pos.current;
    int nextElem = next[current];
    int newElem = allocate();
    elements[newElem] = e;
    next[newElem] = nextElem;
    prev[newElem] = current;
    if (nextElem == -1) {
        tail = newElem;
    }
    else {
        prev[nextElem] = newElem;
    }
    next[current] = newElem;
    pos.current = newElem;
    length++;
}

void IteratedList::addToEnd(TElem e) {
    int newElem = allocate();
    elements[newElem] = e;
    next[newElem] = -1;
    prev[newElem] = tail;
    if (tail == -1) {
        head = newElem;
    }
    else {
        next[tail] = newElem;
    }
    tail = newElem;
    length++;
}

IteratedList::~IteratedList() {
    for (int i = 0; i < cp; i++) {
        if (next[i] != i + 1) {
            deallocate(i);
        }
    }
}

int IteratedList::allocate() {
    int newElem = firstEmpty;
    firstEmpty = next[firstEmpty];
    next[newElem] = -1;
    prev[newElem] = -1;
    return newElem;
}

void IteratedList::deallocate(int i) {
    next[i] = firstEmpty;
    firstEmpty = i;
}
