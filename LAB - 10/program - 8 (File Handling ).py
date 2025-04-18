words_to_remove = ['a', 'the', 'an']

try:
    with open('Exam.txt', 'r') as src:
        content = src.read()

    for word in words_to_remove:
        content = content.replace(f' {word} ', ' ')
        content = content.replace(f' {word}.', '.')
        content = content.replace(f' {word},', ',')
        content = content.replace(f' {word}!', '!')
        content = content.replace(f' {word}?', '?')

    for word in words_to_remove:
        content = content.replace(f'{word} ', '')
        content = content.replace(f' {word}', '')

    content = ' '.join(content.split())

    with open('output.txt', 'w') as dst:
        dst.write(content)
    
    print("Processed content has been written to 'output.txt'.")
except FileNotFoundError:
    print("Error: The file 'Exam.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
