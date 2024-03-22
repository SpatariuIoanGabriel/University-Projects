#include "ListIterator.h"
#include "IteratedList.h"
#include <exception>

ListIterator::ListIterator(const IteratedList& list) : list(list) {
    this->current = list.head;
}

void ListIterator::first() {
    this->current = list.head;
}

void ListIterator::next() {
    if (!valid()) {
        throw std::exception();
    } else {
        this->current = list.next[this->current];
    }
}

bool ListIterator::valid() const {
    return (this->current != -1);
}

TElem ListIterator::getCurrent() const {
    if (!valid()) {
        throw std::exception();
    } else {
        return list.elements[this->current];
    }
}
