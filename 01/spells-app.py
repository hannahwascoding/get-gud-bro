# Create a basic application that allows the user to 
# search for a spell name from the DND JSON Spells.

import json

def card_details(spell):
    print('-' * 50)
    print(f'{spell["name"]:^20} | {spell["range"]:^8} | {spell["duration"]:^10}')
    print('-' * 50)
    print(f'{spell["description"]:<28}')
    print('-' * 50)
    print(f'{spell["level"]:^20} | {spell["type"]:^15}')
    print('-' * 50)
    tags = spell["classes"]
    print('Available for following class:',', '.join(tags))
    print('-' * 50)

#open json file
with open('spells.json', 'r', encoding='utf-8') as f:
    contents = f.read()

#load json file
loadjson = json.loads(contents)

matches = []

while len(matches) < 1:
    # input to find spell name
    spell_search = input('Enter a spell name to find (partial names are allowed): ').strip().lower()

    for spell in loadjson:
        if spell_search in spell["name"].lower():
            matches.append(spell)

    if len(matches) >= 1:
        break
    else:
        print('Error. Spell not found. Please try again.')

print('The following have been found: ')
for i, spell in enumerate(matches, start=1):
    print(f'{i}: {spell["name"]}')

while True:
    spell_select = int(input('Please select a number from the list: '))

    if 1 <= spell_select <= len(matches):
        card_details(matches[spell_select - 1])
        break
