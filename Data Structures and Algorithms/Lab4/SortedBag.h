#pragma once

// DO NOT INCLUDE SORTEDBAGITERATOR

// DO NOT CHANGE THIS PART
typedef int TComp;
typedef TComp TElem;
typedef bool (*Relation)(TComp, TComp);
#define NULL_TCOMP -11111

class SortedBagIterator;

class BSTNode {
private:
    TComp value;
    BSTNode* leftChild;
    BSTNode* rightChild;

public:
    BSTNode();
    BSTNode(TComp value, BSTNode* leftChild, BSTNode* rightChild);

    TComp getValue() const;
    void setValue(TComp value);

    BSTNode* getLeftChild() const;
    void setLeftChild(BSTNode* leftChild);

    BSTNode* getRightChild() const;
    void setRightChild(BSTNode* rightChild);

    bool isNull();

    bool isLeaf();
};

class SortedBag {
    friend class SortedBagIterator;

private:
    BSTNode* root;
    int numberOfElements;
    int capacity;
    int firstFree;
    Relation r;

    void changeFirstFree();
    void resize();



public:
    // constructor
    SortedBag(Relation r);

    // adds an element to the sorted bag
    void add(TComp e);

    // removes one occurrence of an element from the sorted bag
    // returns true if an element was removed, false otherwise (if e was not part of the sorted bag)
    bool remove(TComp e);

    // checks if an element appears in the sorted bag
    bool search(TComp e) const;

    // returns the number of occurrences for an element in the sorted bag
    int nrOccurrences(TComp e) const;

    // returns the number of elements in the sorted bag
    int size() const;

    // returns an iterator for this sorted bag
    SortedBagIterator iterator() const;

    // checks if the sorted bag is empty
    bool isEmpty() const;

    // destructor
    ~SortedBag();
};
