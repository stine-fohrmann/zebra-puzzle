''' Einstein / Zebra Puzzle '''

import random

# Example puzzle: herbalists (possibly unsolvable)

# qualities
# names: Antonius, Domingo, Flavian, Horacio, Lucius
#           a1        a2        a3      a4      a5
# herbs: mandrake root, cinquefoil, rosemary, juniper berries, mistletoe
#           b1              b2          b3          b4              b5
# moon phase: new, first quarter, full, third quarter, waning crescent
#               c1      c2          c3      c4              c5
# amount: a bit, some, standard, a lot, pile
#           d1      d2      d3      d4    d5

# clues
# (1) mandrake root was collected in a standard amount in the third quarter.
# (2) rosemary was collected on a new moon in the maximum possible amount, but not by domingo.
# (3) antonius and horacio were working on either a full moon or the third quarter.
# (4) the juniper berries were collected on the moon's first quarter.
# (5) no one was collecting mistletoe on the two last phases of the moon.
# (6) horacio harvested the smallest possible amount of herbs on a full moon.
# (7) three herbalists - the one who collected only some herbs, another who collected mandrake root,
#     and flavian - were working on first and third quarters of the moon, and also on the waning crescent.

# abstraction
# quality A: a1, ..., a5 -> names
# quality B: b1, ..., b5 -> herbs
# quality C: c1, ..., c5 -> moon phase
# quality D: d1, ..., d5 -> amount

# what the clues mean
# (1) b1 & d3 & c4
# (2) (b3 & c1 & d5) !& a2
# (3) (a1 & c3, a4 & c4) or (a1 & c4, a4 & c3)  //  (a1, a4) &? (c3, c4)
# (4) b4 & c2
# (5) b5 !& c4, b5 !& c5
# (6) a4 & d1 & c3
# (7) (d2, b1, a3) &? (c2, c4, c5)

# clue abstraction notation
# A & B : A belongs to B = B belongs to A
# A !& B : A and B do not belong together
# (A, B) &? (C, D) : A and B belong to C and D, but the exact relations are unknown, short for (A & C, B & D) or (A & D, B & C), from this it follows that A !& B, C !& D

# Additional notation for puzzles with an ordered quality
# A < B : A is directly left of B
# A > B : A is directly right of B
# A << B : A is left of B, but not necessarily right next to B
# A >> B : A is right of B, but not necessarily right next to B
# A <?> B : A and B are directly next to each other




''' Code '''
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

