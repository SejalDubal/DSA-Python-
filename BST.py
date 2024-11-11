class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        # Recursively insert into the left or right subtree
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.value:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    # Pre-order traversal (Root, Left, Right)
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # In-order traversal (Left, Root, Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Post-order traversal (Left, Right, Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    # Search for a node in the binary tree
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.value == key:
            return node

        # Recur down the tree
        if key < node.value:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # Find the minimum value node in the binary tree
    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Delete a node
    def delete(self, root, key):
        # Base case
        if root is None:
            return root

        # Recur down the tree
        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.find_min(root.right)

            # Copy the inorder successor's content to this node
            root.value = temp.value

            # Delete the inorder successor
            root.right = self.delete(root.right, temp.value)

        return root

    # Utility method to start delete operation from the root
    def delete_node(self, key):
        self.root = self.delete(self.root, key)

# Main program to handle user input and perform operations
if __name__ == "__main__":
    bst = BST()

    # Take user input for inserting nodes into the BST
    print("Enter the values to insert into the BST (separate values by spaces):")
    values = list(map(int, input().split()))
    for value in values:
        bst.insert(value)

    # Show the tree's traversals
    print("\nIn-order Traversal (sorted order):")
    bst.inorder(bst.root)
    print("\nPre-order Traversal:")
    bst.preorder(bst.root)
    print("\nPost-order Traversal:")
    bst.postorder(bst.root)

    # Take user input for searching a node
    search_value = int(input("\nEnter a value to search in the tree: "))
    node = bst.search(search_value)
    if node:
        print(f"Node with value {search_value} found in the tree.")
    else:
        print(f"Node with value {search_value} not found in the tree.")

    # Take user input for deleting a node
    delete_value = int(input("\nEnter a value to delete from the tree: "))
    bst.delete_node(delete_value)
    print(f"Tree after deleting node {delete_value}:")
    bst.inorder(bst.root)
    print()
