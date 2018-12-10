import networkx as nx
import matplotlib.pyplot as plot
from multiset import *


class SourceAnalyzer():
    """
    Class for analyzing the flow-graph of a program.
    """

    def __init__(self, graph):
        """
        Constructs a SourceAnalyzer from a graph that should represent the flow
        of the program to analyze.
        """
        self.graph = graph

    def all_pointing_to(self, s):
        """
        Returns a list of all nodes that has an edge that points to 's'
        """
        nodes = []
        for (u, v) in self.graph.edges:
            if v == s:
                nodes.append(u)
        return nodes

    def find_path_between(self, source, target):
        """
        Find alls paths between the 'source' and 'target' nodes. The source and
        the target may be the same node.
        """
        paths = []
        if source == target:
            neighbours = self.all_pointing_to(target)
            for neighbour in neighbours:
                sub_paths = nx.all_simple_paths(self.graph, source, neighbour)
                for sub_path in sub_paths:
                    sub_path.append(source)
                    paths.append(sub_path)
        else:
            sub_paths = nx.all_simple_paths(self.graph, source, target)
            for sub_path in sub_paths:
                paths.append(sub_path)
        return paths

    def is_subpath(self, p0, p1):
        """
        Returns whether or not path 'p0' is a sub-path of 'p1'
        """
        if len(p0) > len(p1):
            return False
        s0 = Multiset(p0)
        s1 = Multiset(p1)
        return s0 == s0.intersection(s1)

    def filter_simple_paths(self, simple_paths):
        """
        Filters a list of simple paths so that only the prime paths remain.
        The list of prime paths are returned
        """
        paths = []
        for p0 in simple_paths:
            add = True
            for p1 in simple_paths:
                if self.is_subpath(p0, p1) and not p0 == p1:
                    add = False
            if add:
                paths.append(p0)
        return paths

    def find_all_paths(self):
        """
        Finds and returns a list of all prime paths in the graph
        """
        paths = []
        for u in self.graph.nodes:
            for v in self.graph.nodes:
                sub_paths = self.find_path_between(u, v)
                for sub_path in sub_paths:
                    paths.append(sub_path)
        return self.filter_simple_paths(paths)

    def plot(self):
        """
        Plot the graph
        """
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx_nodes(self.graph, pos, node_color='y', node_size=600)
        nx.draw_networkx_labels(self.graph, pos)
        nx.draw_networkx_edges(self.graph, pos, arrows=True)
        plot.show()

def analyze_test():
    """
    Test on a simple graph
    """
    # Build a graph
    graph = nx.DiGraph()
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 1)

    # List of correct prime paths for graph
    correct_paths = [
        [0, 1, 2],
        [0, 1, 3, 4],
        [1, 3, 4, 1],
        [3, 4, 1, 3],
        [4, 1, 3, 4],
        [3, 4, 1, 2]
    ]

    # Analyze graph to find prime paths
    analyzer = SourceAnalyzer(graph)
    prime_paths = analyzer.find_all_paths()
    analyzer.plot()

    # Check that all paths were found
    assert len(correct_paths) == len(prime_paths), "The number of prime paths are not correct"
    for p in correct_paths:
        found = False
        for pp in prime_paths:
            if p == pp:
                found = True
        if not found:
            stop = 0
        assert found, "A prime path was not found"

    print "The test graph was correctly analyzed"


def analyze_source():
    analyze_test()


if __name__ == "__main__":
    analyze_source()