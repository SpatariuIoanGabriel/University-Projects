#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

Stack::Stack() {
    elements = nullptr;
    topIndex = -1;
    capacity = 0;
}

Stack::~Stack() {
    delete[] elements;
}

void Stack::push(BSTNode* element) {
    if (topIndex == capacity - 1) {
        // Resize the array
        int newCapacity = capacity == 0 ? 1 : capacity * 2;
        BSTNode** newElements = new BSTNode*[newCapacity];
        for (int i = 0; i <= topIndex; i++) {
            newElements[i] = elements[i];
        }
        delete[] elements;
        elements = newElements;
        capacity = newCapacity;
    }
    topIndex++;
    elements[topIndex] = element;
}

void Stack::pop() {
    if (topIndex >= 0) {
        topIndex--;
    }
}

BSTNode* Stack::top() const {
    if (topIndex >= 0) {
        return elements[topIndex];
    } else {
        return nullptr;
    }
}

bool Stack::empty() const {
    return topIndex == -1;
}

int Stack::getCapacity() const {
    return capacity;
}


SortedBagIterator::SortedBagIterator(const SortedBag& b) : sb(b) {
    currentNode = sb.root;
    while (currentNode != nullptr) {
        stack.push(currentNode);
        currentNode = currentNode->getLeftChild();
    }
}

TComp SortedBagIterator::getCurrent() {
    if (!valid())
        throw std::exception();

    return stack.top()->getValue();
}

bool SortedBagIterator::valid() {
    return !stack.empty();
}

void SortedBagIterator::next() {
    if (!valid())
        throw std::exception();

    BSTNode* current = stack.top();
    stack.pop();

    if (current->getRightChild() != nullptr) {
        currentNode = current->getRightChild();
        while (currentNode != nullptr) {
            stack.push(currentNode);
            currentNode = currentNode->getLeftChild();
        }
    }
}

void SortedBagIterator::first() {
    stack = Stack();
    currentNode = sb.root;
    while (currentNode != nullptr) {
        stack.push(currentNode);
        currentNode = currentNode->getLeftChild();
    }
}
