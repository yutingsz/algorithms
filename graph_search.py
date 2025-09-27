"""Graph search utilities.

This module currently exposes a tiny adjacency-list graph container and a
recursive depth-first search (DFS) implementation.  The goal is to provide a
straightforward, well-documented reference implementation that can be reused in
tests or experiments across the repository.

Example
-------
>>> graph = Graph()
>>> graph.add_edge("A", "B")
>>> graph.add_edge("A", "C")
>>> graph.add_edge("B", "D")
>>> depth_first_search(graph, "A")
['A', 'B', 'D', 'C']

The DFS traversal visits each vertex exactly once, following outgoing edges in
the order they were added.
"""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Deque, Dict, Iterable, List, Set, TypeVar

T = TypeVar("T")


class Graph:
    """A lightweight adjacency-list representation of a graph.

    The graph is undirected by default.  When adding an edge, callers can opt
    into directed semantics by passing ``directed=True``.
    """

    def __init__(self) -> None:
        self._adj: Dict[T, List[T]] = defaultdict(list)

    def add_vertex(self, vertex: T) -> None:
        """Ensure ``vertex`` is present in the adjacency map."""

        self._adj.setdefault(vertex, [])

    def add_edge(self, u: T, v: T, *, directed: bool = False) -> None:
        """Add an edge between ``u`` and ``v``.

        Parameters
        ----------
        u, v:
            Endpoints of the edge.
        directed:
            If ``True`` only the ``u`` -> ``v`` direction is recorded.  When
            ``False`` (the default) the opposite direction ``v`` -> ``u`` is
            also inserted so the graph behaves as undirected.
        """

        self._adj[u].append(v)
        if not directed:
            self._adj[v].append(u)
        else:
            self._adj.setdefault(v, [])

    def neighbors(self, vertex: T) -> Iterable[T]:
        """Return the adjacent vertices for ``vertex``.

        The returned iterable reflects the order in which neighbors were added
        to the graph.
        """

        return tuple(self._adj[vertex])

    def __contains__(self, vertex: object) -> bool:
        return vertex in self._adj


def depth_first_search(graph: Graph, start: T) -> List[T]:
    """Perform a depth-first search starting at ``start``.

    Parameters
    ----------
    graph:
        A :class:`Graph` instance describing the search space.
    start:
        The starting vertex.  ``KeyError`` is raised if the vertex is not part
        of the graph.

    Returns
    -------
    list
        The vertices in the order they were first discovered during the DFS.
    """

    if start not in graph:
        raise KeyError(f"Start vertex {start!r} not present in graph")

    visited: Set[T] = set()
    traversal: List[T] = []

    def dfs(vertex: T) -> None:
        visited.add(vertex)
        traversal.append(vertex)

        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return traversal


def breadth_first_search(graph: Graph, start: T) -> List[T]:
    """Perform a breadth-first search starting at ``start``.

    The algorithm explores the graph in *layers*.  All neighbors at distance 1
    from ``start`` are visited before moving on to distance 2, and so on.  This
    behavior makes BFS useful for computing shortest paths in unweighted graphs
    and for level-order traversals of tree structures.

    Parameters
    ----------
    graph:
        A :class:`Graph` instance describing the search space.
    start:
        The starting vertex.  ``KeyError`` is raised if the vertex is not part
        of the graph.

    Returns
    -------
    list
        The vertices in the order they were first discovered during the BFS.
    """

    if start not in graph:
        raise KeyError(f"Start vertex {start!r} not present in graph")

    visited: Set[T] = {start}
    traversal: List[T] = []
    queue: Deque[T] = deque([start])

    while queue:
        vertex = queue.popleft()
        traversal.append(vertex)

        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal

