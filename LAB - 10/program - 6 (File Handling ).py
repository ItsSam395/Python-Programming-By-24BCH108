try:
    with open('example.txt', 'r') as f1, open('target.txt', 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    with open('merged_file.txt', 'w') as target:
        min_length = min(len(lines1), len(lines2))

        for i in range(min_length):
            target.write(lines1[i])
            target.write(lines2[i])

        if len(lines1) > min_length:
            target.writelines(lines1[min_length:])
        if len(lines2) > min_length:
            target.writelines(lines2[min_length:])

    print(f"Lines from example.txt and target.txt have been merged into merged_file.txt.")
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
    
