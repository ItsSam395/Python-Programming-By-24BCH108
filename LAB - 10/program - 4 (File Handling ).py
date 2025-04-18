import os

source_file = 'example.txt'
target_directory = 'C:\\Users\\iamsh\\OneDrive\\Desktop\\PYHTON'

os.makedirs(target_directory, exist_ok=True)

target_file = os.path.join(target_directory, os.path.basename(source_file))

try:
    with open(source_file, 'rb') as src:
        with open(target_file, 'wb') as dst:
            dst.write(src.read())
    print(f"File '{source_file}' has been copied to '{target_directory}'.")
except FileNotFoundError:
    print(f"Error: The file '{source_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
