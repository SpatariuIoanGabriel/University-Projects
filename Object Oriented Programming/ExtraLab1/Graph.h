#ifndef GRAPH_H
#define GRAPH_H

#include <map>
#include <vector>
#include <queue>
#include <algorithm>

template<typename T, typename Container>
class Graph
{
public:
    Graph();
    void addNode(const T& node);
    void addEdge(const T& node1, const T& node2);
    Container getNeighbours(const T& node) const;
    bool containsNode(const T& node) const;
    std::vector<T> bfs(const T& start, const T& end);

private:
    std::map<T, Container> adjLists;
};

#include "Graph.cpp"

#endif
