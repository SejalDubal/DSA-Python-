class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued {value} to the queue.")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_value

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.front.value

    # Check if queue is empty
    def is_empty(self):
        return self.front is None

    # Display queue contents
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        current = self.front
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    queue = Queue()

    # User input for queue operations
    while True:
        choice = input("Enter 'enqueue' to enqueue, 'dequeue' to dequeue, 'peek' to peek, 'exit' to exit: ").lower()
        if choice == "enqueue":
            value = int(input("Enter the value to enqueue: "))
            queue.enqueue(value)
        elif choice == "dequeue":
            dequeued_value = queue.dequeue()
            if dequeued_value is not None:
                print(f"Dequeued {dequeued_value} from the queue.")
        elif choice == "peek":
            front_value = queue.peek()
            if front_value is not None:
                print(f"Front of queue: {front_value}")
        elif choice == "exit":
            break
        else:
            print("Invalid choice! Please enter again.")
