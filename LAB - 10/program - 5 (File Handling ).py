try:
    with open('example.txt', 'r') as src:
    
        with open('target.txt', 'w') as dst:
            dst.write(src.read().upper())
        
        print(f"Contents of example.txt have been copied to target_file with uppercase characters.")
except FileNotFoundError:
    print(f"Error: The file '{source_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

