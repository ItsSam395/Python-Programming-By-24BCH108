class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.items[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents:", self.items)

def main():
    stack = Stack()
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter the item to push: ")
            stack.push(item)
        elif choice == '2':
            popped_item = stack.pop()
            if popped_item is not None:
                print(f"Popped item: {popped_item}")
        elif choice == '3':
            top_item = stack.peek()
            if top_item is not None:
                print(f"Top item: {top_item}")
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()
