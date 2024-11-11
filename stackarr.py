class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, value):
        self.stack.append(value)
        print(f"Pushed {value} onto the stack.")

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        popped_value = self.stack.pop()
        return popped_value

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack contents
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        print("Stack contents:", self.stack)

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
