import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from BST import RedBlackBST


def build_sample_tree():
    tree = RedBlackBST()
    entries = [
        ("t", 10),
        ("d", 30),
        ("c", 40),
        ("a", 11),
        ("e", 22),
        ("f", 3),
    ]
    for key, value in entries:
        tree.put_main(key, value)
    return tree


def test_get_returns_inserted_values():
    tree = build_sample_tree()

    assert tree.get_main("t") == 10
    assert tree.get_main("d") == 30
    assert tree.get_main("f") == 3
    assert tree.get_main("missing") is None


def test_updating_existing_key_does_not_change_size():
    tree = RedBlackBST()
    tree.put_main("k", 1)
    tree.put_main("a", 2)

    original_size = tree.size(tree.root)

    tree.put_main("k", 99)

    assert tree.get_main("k") == 99
    assert tree.size(tree.root) == original_size
