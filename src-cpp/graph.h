#ifndef GRAPH_H
#define GRAPH_H

#include <vector>
#include <set>

template <typename T>
class Graph {
    public:
        // Ctors
        Graph(std::vector<T> vertices);
        Graph(T* vertices);
        // Methods
        void add_vertex(T vertex);
        void add_edge(T vertex1, T vertex2);
        bool has_vertex(T vertex) const;
        bool has_edge(T vertex) const;
        void delete_vertex(T vertex);
        void delete_edge(T vertex);

        int degree(vertex);
        vector<int> get_neighbors(const T& vertex) const; 
    private:
        std::set<T> m_vertices;
        std::set<T> m_adj_lists;
};

template<typename T>
class SimpleGraph : Graph {
};

template<typename T>
class DirectedGraph : Graph {
};

template<typename T>
class WeightedGraph : Graph { 
};

template<typename T>
class DirectedWeightedGraph : DirectedGraph {
};

#endif
