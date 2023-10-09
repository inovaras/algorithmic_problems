import requests
from pprint import pprint

with open('input.txt') as file:
    s = file.read()
lst = s.split('\n')
answer = []
for number in lst:
    response = requests.get(f'http://numbersapi.com/{number}/math?json=true')
    pprint(response.json())
    if response.json()['found']:
        answer.append('Interesting')
    else:
        answer.append('Boring')

with open('output.txt', 'w') as file:
    file.write('\n'.join(answer))


