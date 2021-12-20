class Node:

    def __init__(self, value):
        self.lc = None
        self.rc = None
        self.parent = None
        self.value = value

    def set_left(self, node):
        self.lc = node
        node.parent = self

    def set_right(self, node):
        self.rc = node
        node.parent = self

    def make_leaf(self, value):
        self.value = value
        self.lc = None
        self.rc = None

    def is_leaf(self):
        return not self.is_pair()

    def is_pair(self):
        return self.value is None

    def is_root(self):
        return self.parent is None

    def depth(self):
        cur = self
        d = 0
        while not cur.is_root():
            d += 1
            cur = cur.parent

        return d

    # print as list representation like in description
    def __str__(self):
        if self.is_pair():
            return f'[{self.lc},{self.rc}]'
        else:
            return str(self.value)

    def get_leaves(self):
        leaves = []
        self._get_leaves_aux(leaves)
        return leaves

    def _get_leaves_aux(self, lst: list):
        if self.is_leaf():
            lst.append(self)

        if self.is_pair():
            self.lc._get_leaves_aux(lst)
            self.rc._get_leaves_aux(lst)

    # copied off of internet
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.rc is None and self.lc is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.rc is None:
            lines, n, p, x = self.lc._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.lc is None:
            lines, n, p, x = self.rc._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.lc._display_aux()
        right, m, q, y = self.rc._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class Action:

    def __init__(self, verifier, actioner, name):
        self.verifier = verifier
        self.actioner = actioner
        self.name = name

    def __str__(self):
        return self.name

    def perform_action(self, tree) -> bool:
        actionable = find_node(tree, self.verifier)
        if actionable:
            print(f'actioned: {actionable}')
        if actionable:
            self.actioner(actionable)
            return True
        else:
            return False

def parse(txt: iter) -> Node:

    """
    Yes, I know i could have just used eval to do this simply, but my friend is using C++
    and had no choice but to learn how to parse this thing so I decided to accompany him
    on this journey.
    """

    char = next(txt)

    if char == '[':
        lc = parse(txt)
        next(txt)  # skip ,
        rc = parse(txt)
        next(txt)  # skip ]

        node = Node(None)
        node.set_left(lc)
        node.set_right(rc)
        return node

    # literal
    else:
        return Node(int(char))

def explode(node):

    # keep track of the modes that were modified
    left_set = False
    right_set = False

    cur = node.parent
    while cur and (not left_set or not right_set):

        if cur.lc.is_leaf() and not left_set:
            cur.lc.value += node.lc.value
            left_set = True

        if cur.rc.is_leaf() and not right_set:
            cur.rc.value += node.rc.value
            right_set = True

        cur = cur.parent

    # make the node a leaf
    node.make_leaf(0)

def explode_gud(node: Node):

    lval = node.lc.value
    rval = node.rc.value

    node.make_leaf(0)

    root = node
    while root.parent:
        root = root.parent

    leaves = root.get_leaves()

    # get index pos of
    node_index_pos = [idx for idx, leaf in enumerate(leaves) if leaf is node][0]

    adjacent_left = leaves[node_index_pos-1] if node_index_pos-1 >= 0 else None
    adjacent_right = leaves[node_index_pos+1] if node_index_pos+1 < len(leaves) else None

    if adjacent_right:
        adjacent_right.value += rval

    if adjacent_left:
        adjacent_left.value += lval

def split(node):
    left_val = node.value // 2
    right_val = left_val if node.value % 2 == 0 else left_val + 1

    node.value = None
    node.set_left(Node(left_val))
    node.set_right(Node(right_val))

def should_explode(node: Node):
    return node.is_pair() and node.depth() >= 4

def should_split(node: Node):
    return node.is_leaf() and node.value >= 10

def find_node(node: Node, predicate):

    # check if found
    if predicate(node):
        return node

    if node.is_pair():
        found_left = find_node(node.lc, predicate)
        if found_left is not None:
            return found_left
        found_left = find_node(node.rc, predicate)
        if found_left is not None:
            return found_left

    return None

def reduce(tree: Node):

    actions = [Action(should_explode, explode_gud, "explode"), Action(should_split, split, "split")]

    done = False
    while not done:
        any_performed = False
        for action in actions:

            # perform action
            if not any_performed:
                performed = action.perform_action(tree)
                any_performed |= performed

                if performed:
                    print(f'after {action}: {tree}')
                    tree.display()

        done = not any_performed

def magnitude(tree: Node):

    if tree.is_leaf():
        return tree.value

    return 3 * magnitude(tree.lc) + 2 * magnitude(tree.rc)

def concat(t1, t2):
    new_root = Node(None)
    new_root.set_left(t1)
    new_root.set_right(t2)
    return new_root

if __name__ == "__main__":

    lines = [s.strip() for s in open('input.txt').readlines()]

    max_mag = 0

    for l1 in lines:
        for l2 in lines:
            if l1 != l2:
                t1 = parse(l1.__iter__())
                t2 = parse(l2.__iter__())
                concated = concat(t1, t2)
                reduce(concated)
                mag = magnitude(concated)

                max_mag = max(mag, max_mag)

    print(max_mag)




