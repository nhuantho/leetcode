"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        node_res: Node = Node(node.val)
        visited_nodes = dict()

        def travel(node: Optional['Node'], node_res: Node):
            if node.neighbors is None:
                return

            visited_nodes.update({node.val: node_res})
            node_res.neighbors = []

            for neighbor in node.neighbors:
                neighbor_res = Node(neighbor.val)
                if neighbor.val in visited_nodes:
                    node_res.neighbors.append(visited_nodes[neighbor.val])
                    continue
                node_res.neighbors.append(neighbor_res)
                travel(neighbor, neighbor_res)

        travel(node, node_res)

        return node_res