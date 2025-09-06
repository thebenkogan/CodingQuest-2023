from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Optional
from aoc import read_input


@dataclass
class Node:
    item_id: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, item_id):
        new_node = Node(item_id)
        if self.root == None:
            self.root = new_node
            return

        curr = self.root
        while True:
            if item_id >= curr.item_id:
                if curr.right == None:
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                if curr.left == None:
                    curr.left = new_node
                    return
                curr = curr.left

    def max_depth(self):
        if self.root == None:
            return 0

        stack = [(1, self.root)]
        best = 0
        while len(stack) > 0:
            d, n = stack.pop()
            best = max(best, d)

            if n.left != None:
                stack.append((d + 1, n.left))
            if n.right != None:
                stack.append((d + 1, n.right))

        return best

    def max_width(self):
        if self.root == None:
            return 0

        level_count = defaultdict(int)
        q = deque([(0, self.root)])
        while len(q) > 0:
            d, n = q.popleft()
            level_count[d] += 1

            if n.left != None:
                q.append((d + 1, n.left))
            if n.right != None:
                q.append((d + 1, n.right))

        print(level_count)
        return max(level_count.values())


ns = [int(n, 16) for n in read_input()]
bst = BST()
for n in ns:
    bst.insert(n)

print(bst.max_width() * bst.max_depth())
