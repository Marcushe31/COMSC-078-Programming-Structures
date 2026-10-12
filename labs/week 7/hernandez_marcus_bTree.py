# Name: Marcus Hernandez
# COMSC-078
# Assignment: Week 7 Lab (Trees and Dictionaries), Part 1 - Trees
# Description: Makes the tree from the picture, then prints the tree,
# its label, its branches, and how many leaves it has.

def tree(root_label, branches=[]):
    """Returns a tree with the given root label and list of branches."""
    return [root_label] + list(branches)

def label(tree):
    """Returns the root label of a tree."""
    return tree[0]

def branches(tree):
    """Returns the list of branches of a tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the tree has no branches."""
    return not branches(tree)

def count_leaves(tree):
    """Returns the number of leaves in a tree."""
    if is_leaf(tree):
        return 1
    # if it's not a leaf, then we just go through every branch and count
    # its leaves too, and adding all of those up gives the total for the tree
    return sum([count_leaves(b) for b in branches(tree)])

def main():
    """Build the tree and print its parts."""
    # the root is 4, and it has two branches: 2 (which has the
    # leaves 1 and 3 under it) and 6 (which only has the leaf 5 under it)
    t = tree(4, [tree(2, [tree(1), tree(3)]), tree(6, [tree(5)])])

    print('Tree:', t)
    print('Label:', label(t))
    print('Branches:', branches(t))
    print('Number of leaves:', count_leaves(t))

main()