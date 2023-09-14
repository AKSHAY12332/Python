import os

print(os.getcwd())
print(os.listdir('C:\\users'))

import shutil

shutil.move('C:\\Users\\2068301\\Downloads\\cinema.py','C:\\Users\\2068301\\IdeaProjects\\PythonFolder')

file_path = 'C:\\Users\\2068301\\Documents\\Example_Top_Level'

for folder, sub_folders, files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("\n")
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print(f"\tSubfolder: {sub_fold}")

    print("\n")
    print('The files are: ')
    for f in files:
        print(f"\tFiles are: {f}")
    print("\n")

from datetime import datetime, date

mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)


today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())


import datetime
mytime = datetime.time(13,20,1,20)

print(mytime.minute)


import math
import random

print(random.uniform(a=0, b=100))
print(random.gauss(mu=0, sigma=1))

# Regular Expressions

import re

text = 'The agent\'s phone number is phone 408-555-124. Call soon!'

pattern = 'phone'
match = re.search(pattern, text)
print(match)
print(match.span())
print(match.start())
print(match.end())

matches = re.findall('phone',text)
print(matches)
print(len(matches))

print()
for match in re.finditer('phone',text):
    print(match.span())
    print(match.group())

text = 'My phone number is 408-555-1234'

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
print(phone.group())

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())
print(results.group(2))

one = re.search(r'cat|dog', 'The cat is here')
two = re.findall(r'.at','The cat in the hat went splat.')
print(one)
print()
print(two)
three = re.findall(r'..at', 'The cat in the hat went splat. ')
print(three)
print('\n\n')

phrase = 'there are 34 numbers inside 5 this sentence'
pattern = r'[^\d]+'
print(re.findall(pattern,phrase))
print('\n')

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
pattern = r'[^!?. ]+'
clean = re.findall(pattern,test_phrase)
print(clean)
print(' '.join(clean))

print()
text = 'Only find the hyphen-words in this sentence. But you do not know how long-ish they are.'
pattern = r'\w+-\w+'
print(re.findall(pattern, text))

print()
text = 'Hello, would you like some catfish?'
texttwo = 'Hello, would you like to take a catnap?'
textthree = 'Hello, have you seen this caterpillar'
print(re.search(r'cat(fish|nap|erpillar)',textthree))
