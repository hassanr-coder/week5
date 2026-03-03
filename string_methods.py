'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 5 Assignment 3
'''
def count_substing(text, sub):
    return text.count(sub)  

def replace_text(text, old, new):
    return text.replace(old, new)

text = input("Enter a sentence: ") 

sub = input("Enter a word to count: ")
count = count_substing(text, sub)
print("The substring appears", count, "times.")

old_text= input("Enter the word to replace: ")
new_text = input("Enter the new word: ")

updated_text = replace_text(text, old_text, new_text)
print("Updated sentence:", updated_text)