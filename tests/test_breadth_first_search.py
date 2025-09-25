from pathlib import Path
import sys

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from graph_search import Graph, breadth_first_search


def test_breadth_first_search_traversal_order():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")

    assert breadth_first_search(graph, "A") == ["A", "B", "C", "D", "E"]


def test_breadth_first_search_handles_directed_edges():
    graph = Graph()
    graph.add_edge(1, 2, directed=True)
    graph.add_edge(2, 3, directed=True)
    graph.add_vertex(4)

    assert breadth_first_search(graph, 1) == [1, 2, 3]


def test_breadth_first_search_missing_start_vertex():
    graph = Graph()
    graph.add_vertex("existing")

    with pytest.raises(KeyError):
        breadth_first_search(graph, "missing")
