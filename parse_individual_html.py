# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 12:29:01 2023

@author: sh001
"""

from bs4 import BeautifulSoup

# Read the HTML file
# Note that the path should always have / slash. 
# Enter the path to your html file in html_file_path parameter.
html_file_path = 'C:/shilpa/abc.html'
with open(html_file_path, 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# The text you want to count occurrences of
target_text = "2022/"
target_text2 = "2023/"

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all occurrences of the target text in the parsed HTML
occurrences = soup.find_all(string=lambda text: target_text in text.lower())
occurrences2 = soup.find_all(string=lambda text: target_text2 in text.lower())

# Count the number of occurrences
count = len(occurrences)
count2 =len(occurrences2)

print(f"The text '{target_text}' appears {count} times in the HTML file.")
print(f"The text '{target_text2}' appears {count2} times in the HTML file.")
