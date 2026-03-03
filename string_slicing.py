'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 5 Assignment 1
'''
def extract_character(text, start, length):
    end = start + length
    return text[start:end] 

def reverse_string(text):
    return text[::-1]   

user_text = input("Enter a string: ")

start_index = int(input("Enter the starting index: "))
length =int(input("Enter the length: "))

extracted = extract_character(user_text, start_index, length)

reversed_text = reverse_string(user_text)
print("\nResults:")
print("Extracted substring:", extracted)
print("Reversed string:", reversed_text)

