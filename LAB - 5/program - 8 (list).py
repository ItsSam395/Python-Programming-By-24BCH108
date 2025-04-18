class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item} to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.items[0]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contents:", self.items)

def main():
    queue = Queue()
    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
        elif choice == '2':
            dequeued_item = queue.dequeue()
            if dequeued_item is not None:
                print(f"Dequeued item: {dequeued_item}")
        elif choice == '3':
            front_item = queue.peek()
            if front_item is not None:
                print(f"Front item: {front_item}")
        elif choice == '4':
            queue.display()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()
