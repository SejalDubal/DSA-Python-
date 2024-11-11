class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {value} onto the stack.")

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.value

    # Check if stack is empty
    def is_empty(self):
        return self.top is None

    # Display stack contents
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    stack = Stack()

    # User input for stack operations
    while True:
        choice = input("Enter 'push' to push, 'pop' to pop, 'peek' to peek, 'exit' to exit: ").lower()
        if choice == "push":
            value = int(input("Enter the value to push onto the stack: "))
            stack.push(value)
        elif choice == "pop":
            popped_value = stack.pop()
            if popped_value is not None:
                print(f"Popped {popped_value} from the stack.")
        elif choice == "peek":
            top_value = stack.peek()
            if top_value is not None:
                print(f"Top of stack: {top_value}")
        elif choice == "exit":
            break
        else:
            print("Invalid choice! Please enter again.")
