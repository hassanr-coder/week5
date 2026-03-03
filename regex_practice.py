'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 5 Assignment 4
'''
import re

def extract_phone_numbers(text):
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    return re.findall(pattern, text)

def is_valid_email(email):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.match(pattern, email) is not None

print("===Phone Number Extraction===")
text = input("Enter a block of text: ")

phones = extract_phone_numbers(text)
print("\nPhone numbers found:", phones)
print("Total found:", len(phones))

print("\n=== Email Validator ===")
email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")

