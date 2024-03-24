#include "Graph.h"

template<typename T, typename Container>
Graph<T, Container>::Graph() {}

template<typename T, typename Container>
void Graph<T, Container>::addNode(const T& node)
{
    adjLists[node] = Container();
}

template<typename T, typename Container>
void Graph<T, Container>::addEdge(const T& node1, const T& node2)
{
    if (containsNode(node1) == 0)
    {
        addNode(node1);
    }
    if (containsNode(node2) == 0)
    {
        addNode(node2);
    }
    adjLists[node1].push_back(node2);
    adjLists[node2].push_back(node1);
}

template<typename T, typename Container>
Container Graph<T, Container>::getNeighbours(const T& node) const
{
    return adjLists.at(node);
}

template<typename T, typename Container>
bool Graph<T, Container>::containsNode(const T& node) const
{
    return adjLists.find(node) != adjLists.end();
}

template<typename T, typename Container>
std::vector<T> Graph<T, Container>::bfs(const T& start, const T& end)
{
    std::queue<T> q;
    std::map<T, bool> visited;
    std::map<T, T> parents;
    std::vector<T> path;
    q.push(start);
    visited[start] = true;
    while (!q.empty())
    {
        T current = q.front();
        q.pop();
        if (current == end)
        {
            T temp = end;
            while (temp != start)
            {
                path.push_back(temp);
                temp = parents[temp];
            }
            path.push_back(start);
            reverse(path.begin(), path.end());
            return path;
        }
        else
        {
            for (T neighbour : adjLists[current])
            {
                if (!visited[neighbour])
                {
                    visited[neighbour] = true;
                    parents[neighbour] = current;
                    q.push(neighbour);
                }
            }
        }
    }
    return path;
}
