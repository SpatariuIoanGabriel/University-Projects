#include "SortedBag.h"
#include "SortedBagIterator.h"

SortedBag::SortedBag(Relation r) {
    root = nullptr;
    numberOfElements = 0;
    capacity = 0;
    firstFree = -1;
    this->r = r;
}

void SortedBag::add(TComp e) {
    BSTNode* newNode = new BSTNode(e, nullptr, nullptr);

    if (root == nullptr) {
        root = newNode;
    } else {
        BSTNode* current = root;
        BSTNode* parent = nullptr;

        while (current != nullptr) {
            parent = current;

            if (r(e, current->getValue())) {
                current = current->getLeftChild();
            } else {
                current = current->getRightChild();
            }
        }

        if (r(e, parent->getValue())) {
            parent->setLeftChild(newNode);
        } else {
            parent->setRightChild(newNode);
        }
    }

    numberOfElements++;
}

bool SortedBag::remove(TComp e) {
    if (isEmpty()) {
        return false;  // Bag is empty, nothing to remove
    }

    BSTNode* parent = nullptr;
    BSTNode* current = root;

    while (current != nullptr) {
        if (e == current->getValue()) {
            break;  // Found the element
        }
        parent = current;
        if (r(e, current->getValue())) {
            current = current->getLeftChild();
        } else {
            current = current->getRightChild();
        }
    }

    if (current == nullptr) {
        return false;  // Element not found
    }

    if (current->isLeaf()) {
        if (parent == nullptr) {
            root = nullptr;
        } else if (parent->getLeftChild() == current) {
            parent->setLeftChild(nullptr);
        } else {
            parent->setRightChild(nullptr);
        }
        delete current;
        numberOfElements--;
        return true;  // Element removed
    }

    if (current->getLeftChild() == nullptr) {
        if (parent == nullptr) {
            root = current->getRightChild();
        } else if (parent->getLeftChild() == current) {
            parent->setLeftChild(current->getRightChild());
        } else {
            parent->setRightChild(current->getRightChild());
        }
        delete current;
        numberOfElements--;
        return true;  // Element removed
    }

    if (current->getRightChild() == nullptr) {
        if (parent == nullptr) {
            root = current->getLeftChild();
        } else if (parent->getLeftChild() == current) {
            parent->setLeftChild(current->getLeftChild());
        } else {
            parent->setRightChild(current->getLeftChild());
        }
        delete current;
        numberOfElements--;
        return true;  // Element removed
    }

    BSTNode* successor = current->getRightChild();
    BSTNode* successorParent = current;

    while (successor->getLeftChild() != nullptr) {
        successorParent = successor;
        successor = successor->getLeftChild();
    }

    current->setValue(successor->getValue());

    if (successorParent->getLeftChild() == successor) {
        if (successor->getRightChild() != nullptr) {
            successorParent->setLeftChild(successor->getRightChild());
        } else {
            successorParent->setLeftChild(nullptr);
        }
    } else {
        if (successor->getRightChild() != nullptr) {
            successorParent->setRightChild(successor->getRightChild());
        } else {
            successorParent->setRightChild(nullptr);
        }
    }

    delete successor;
    numberOfElements--;
    return true;  // Element removed
}

bool SortedBag::search(TComp elem) const {
    BSTNode* current = root;
    while (current != nullptr) {
        if (current->getValue() == elem) {
            return true;
        } else if (r(elem, current->getValue())) {
            current = current->getLeftChild();
        } else {
            current = current->getRightChild();
        }
    }
    return false;
}

int SortedBag::nrOccurrences(TComp elem) const {
    BSTNode* current = root;
    int count = 0;
    while (current != nullptr) {
        if (current->getValue() == elem) {
            count++;
        }
        if (r(elem, current->getValue())) {
            current = current->getLeftChild();
        } else {
            current = current->getRightChild();
        }
    }
    return count;
}

int SortedBag::size() const {
    return numberOfElements;
}

bool SortedBag::isEmpty() const {
    return numberOfElements == 0;
}

SortedBagIterator SortedBag::iterator() const {
    return SortedBagIterator(*this);
}

SortedBag::~SortedBag() {
}

BSTNode::BSTNode() {
    value = NULL_TCOMP;
    leftChild = nullptr;
    rightChild = nullptr;
}

BSTNode::BSTNode(TComp value, BSTNode* leftChild, BSTNode* rightChild) {
    this->value = value;
    this->leftChild = leftChild;
    this->rightChild = rightChild;
}

TComp BSTNode::getValue() const {
    return value;
}

void BSTNode::setValue(TComp value) {
    this->value = value;
}

BSTNode* BSTNode::getLeftChild() const {
    return leftChild;
}

void BSTNode::setLeftChild(BSTNode* leftChild) {
    this->leftChild = leftChild;
}

BSTNode* BSTNode::getRightChild() const {
    return rightChild;
}

void BSTNode::setRightChild(BSTNode* rightChild) {
    this->rightChild = rightChild;
}

bool BSTNode::isNull() {
    return value == NULL_TCOMP;
}

bool BSTNode::isLeaf() {
    return leftChild == nullptr && rightChild == nullptr;
}
