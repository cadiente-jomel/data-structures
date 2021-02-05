# Binary Search Tree

* every node has at most 2 child nodes


*  binary search tree or BST
    *  elements has some kind of order
    * all the node on the left hand side of the tree should be less than to its parent node
    * all the node on the right hand side of the tree should be greater than to its parent node
* elements are not duplicated


## Search complexity 
* ___O(log n)___
* ___O(1)___ when the central index would directly match the desired value.

## insert complexity
* ___0(log n)___

## Traversal Technique
* Breadth First Search (BFS)
* Depth First Search (DFS)
    * In order traversal
        * visit left sub-tree, root node, right sub-tree
    * Pre order traversal
        * Root Node First, left sub-tree and then right sub-tree
    * Post order traversal
        * left sub-tree, right sub-tree and then root node

