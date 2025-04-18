def covert_to_words(val):
    words = [
        "zero", "one", "two", "three", "four", 
        "five", "six", "seven", "eight", "nine", 
        "ten", "eleven", "twelve", "thirteen", "fourteen", 
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    if 0 <= val < len(words):
        return words[val]
    else:
        return "Invalid Input"

num = int(input("Enter a number between 0 and 19: "))
print(f"The number {num} in words is: {covert_to_words(num)}")
