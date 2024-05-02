''' Einstein / Zebra Puzzle '''

import random

# specify the qualities
#qualitya = ['Justus', 'Peter', 'Bob', 'Tante Mathilda', 'Onkel Titus'] # persons
#qualityb = ['Wecker', 'Uhr', 'Vase', 'Büste', 'Totenkopf'] # objects
#qualityc = ['morgens', 'vormittags', 'mittags', 'nachmittags', 'abends'] # time
#qualityd = ['Schrottplatz', 'Bibliothek', 'Supermarkt', 'Zentrale', 'Auto'] # place

qualitya = ['Professor Layton', 'Luke', 'Flora', 'Emmy', 'Descole'] # persons
qualityb = ['tea', 'coffee', 'water', 'juice', 'hot chocolate'] # drinks
qualityc = ['biscuit', 'scone', 'piece of cake', 'nothing', 'cookie'] # snack
qualityd = ['green', 'blue', 'yellow', 'red', 'orange'] # chair colours

qualities = [qualitya, qualityb, qualityc, qualityd]


# reorder each quality randomly
for q in qualities:
    random.shuffle(q)

# reorder qualities themselves
random.shuffle(qualities)

# assign abstractions to qualities
[a1, a2, a3, a4, a5] = qualities[0]
[b1, b2, b3, b4, b5] = qualities[1]
[c1, c2, c3, c4, c5] = qualities[2]
[d1, d2, d3, d4, d5] = qualities[3]

# specify clues puzzle 1
clue1 = f'{b1} & {d3} & {c4}'
clue2 = f'({b3} & {c1} & {d5}) !& {a2}'
clue3 = f'({a1}, {a4}) &? ({c3}, {c4})'
clue4 = f'{b4} & {c2}'
clue5 = f'{b5} !& {c4}, {b5} !& {c5}'
clue6 = f'{a4} & {d1} & {c3}'
clue7 = f'({d2}, {b1}, {a3}) &? ({c2}, {c4}, {c5})'
clues = [clue1, clue2, clue3, clue4, clue5, clue6, clue7]

# reorder the clues randomly
random.shuffle(clues)

# replace abstractions with meaningful words

# print the clues
for i in range(len(clues)):
    print(f'clue {i+1}: {clues[i]}')

