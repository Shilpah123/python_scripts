# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 23:17:30 2023

@author: sh001
"""

"""
This script will parse through all the HTML files placed at the path mentioned in html_dir.
Counts the occurences of target_text and target_text2 and prints the output.
"""

from bs4 import BeautifulSoup
import os

# Specify the directory containing your HTML files
# Note that the path should always have / slash. 
html_dir = 'C:/shilpa/'

# Specify the text you want to count occurrences of
target_text = "2023/"
target_text2 = "2022/"

# Initialize a counter
count = 0
count2 = 0

# Iterate through each HTML file in the directory
for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        with open(os.path.join(html_dir, filename), 'r', encoding='utf-8') as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            text_occurrences = soup.find_all(string=lambda text:target_text in text.lower())
            count += len(text_occurrences)

print(f'The text "{target_text}" appears {count} times in the HTML files.')

# Iterate through each HTML file in the directory
for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        with open(os.path.join(html_dir, filename), 'r', encoding='utf-8') as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            text_occurrences2 = soup.find_all(string=lambda text:target_text2 in text.lower())
            count2 += len(text_occurrences2)

print(f'The text "{target_text2}" appears {count2} times in the HTML files.')