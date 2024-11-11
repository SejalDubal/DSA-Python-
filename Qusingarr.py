class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, value):
        self.queue.append(value)
        print(f"Enqueued {value} to the queue.")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        dequeued_value = self.queue.pop(0)
        return dequeued_value

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display queue contents
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Queue contents:", self.queue)

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
