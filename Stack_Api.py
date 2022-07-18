"""Code shows how to consume an API"""
"""Reference api.stackexchange.com"""

import requests
import json

response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

items = response.json()['items'] # data retrieved in json format!

for question in items: # for loop to iterate over the items

    print(question['title']) # searching/getting from the titles
    print(question['link']) # searching/getting from the links
    print()

for question in items:

    if 'python' in question['tags']: # searching for any python tags in the tag item

        print(question['tags']) # gets/retrieves a list of the tags

    if question['answer_count'] >= 2 and question['tags'] == 'python':

        print(question['link']) # gets/retrieves a list of the links associated with the tag

    else:

        print('skipped') # skip if condition is not satisfied!
    
    print()





