''' Zebra / Einstein Puzzle '''

import random

# Example puzzle: Zebrarätsel (one ordered quality)

# qualities
# Häuser: 1, 2, 3, 4, 5 -> a1, a2, a3, a4, a5
# Farben: gelb, blau, rot, grün, weiß
#           b1,  b2,   b3,  b4,   b5
# Nationalitäten: Norweger, Ukrainer, Engländer, Japaner, Spanier
#                    c1,        c2,       c3,       c4,     c5
# Getränke: Wasser, Tee, Milch, Kaffee, O-Saft
#             d1,    d2,   d3,    d4,     d5
# Zigaretten: Kools, Chesterfield, Old Gold, Parliament, Lucky Strike
#               e1,         e2,       e3,       e4,           e5
# Haustiere: Fuchs, Pferd, Schnecken, Zebra, Hund
#               f1,   f2,     f3,       f4,   f5

# clues
# (1) Es gibt fünf Häuser.
# (2) Der Engländer wohnt im roten Haus.
# (3) Der Spanier hat einen Hund.
# (4) Kaffee wird im grünen Haus getrunken.
# (5) Der Ukrainer trinkt Tee.
# (6) Das grüne Haus ist direkt links vom weißen Haus.
# (7) Der Raucher von Old-Gold-Zigaretten hält Schnecken als Haustiere.
# (8) Die Zigaretten der Marke Kools werden im gelben Haus geraucht.
# (9) Milch wird im mittleren Haus getrunken.
# (10) Der Norweger wohnt im ersten Haus.
# (11) Der Mann, der Chesterfields raucht, wohnt neben dem Mann mit dem Fuchs.
# (12) Die Marke Kools wird geraucht im Haus neben dem Haus mit dem Pferd.
# (13) Der Lucky-Strike-Raucher trinkt am liebsten Orangensaft.
# (14) Der Japaner raucht Zigaretten der Marke Parliaments.
# (15) Der Norweger wohnt neben dem blauen Haus.
# (16) Der Chesterfields-Raucher hat einen Nachbarn, der Wasser trinkt.
# Frage: Wer trinkt Wasser? Wem gehört das Zebra?

# clues abstraction
# (2) c3 & b3
# (3) c5 & f5
# (4) d4 & b4
# (5) c2 & d2
# (6) b4 < b5
# (7) e3 & f3
# (8) e1 & b1
# (9) d3 & a3
# (10) c1 & a1
# (11) e2 <?> f1
# (12) e1 <?> f2
# (13) e5 & d5
# (14) c4 & e4
# (15) c1 <?> b2
# (16) e2 <?> d1
# question: d1?, f4?

''' Code '''
# specify the qualities
# qualitya = ['Haus 1', 'Haus 2', 'Haus 3', 'Haus 4', 'Haus 5']   # ordered quality
qualitya = ['house 1', 'house 2', 'house 3', 'house 4', 'house 5']   # ordered quality
# qualityb = ['gelb', 'blau', 'rot', 'grün', 'weiß']
qualityb = ['yellow', 'blue', 'red', 'green', 'white']
# qualityc = ['Norweger', 'Ukrainer', 'Engländer', 'Japaner', 'Spanier']
qualityc = ['norwegian', 'ukranian', 'english', 'japanese', 'spanish']
# qualityd = ['Wasser', 'Tee', 'Milch', 'Kaffee', 'O-Saft']
qualityd = ['water', 'tea', 'milk', 'coffee', 'orange juice']
qualitye = ['Kools', 'Chesterfield', 'Old Gold', 'Parliament', 'Lucky Strike']
# qualityf = ['Fuchs', 'Pferd', 'Schnecken', 'Zebra', 'Hund']
qualityf = ['fox', 'horse', 'snails', 'zebra', 'dog']
qualities = [qualitya, qualityb, qualityc, qualityd, qualitye, qualityf]
qualities_to_be_shuffled = [qualityb, qualityc, qualityd, qualitye, qualityf]

# reorder each quality randomly
for q in qualities_to_be_shuffled:
    random.shuffle(q)

# reorder qualities
random.shuffle(qualities_to_be_shuffled)

# assign abstractions to qualities
[a1, a2, a3, a4, a5] = qualitya
[b1, b2, b3, b4, b5] = qualityb
[c1, c2, c3, c4, c5] = qualityc
[d1, d2, d3, d4, d5] = qualityd
[e1, e2, e3, e4, e5] = qualitye
[f1, f2, f3, f4, f5] = qualityf

# specify clues puzzle 1
clue02 = f'{c3} & {b3}'
clue03 = f'{c5} & {f5}'
clue04 = f'{d4} & {b4}'
clue05 = f'{c2} & {d2}'
clue06 = f'{b4} < {b5}'
clue07 = f'{e3} & {f3}'
clue08 = f'{e1} & {b1}'
clue09 = f'{d3} & {a3}'
clue10 = f'{c1} & {a1}'
clue11 = f'{e2} <?> {f1}'
clue12 = f'{e1} <?> {f2}'
clue13 = f'{e5} & {d5}'
clue14 = f'{c4} & {e4}'
clue15 = f'{c1} <?> {b2}'
clue16 = f'{e2} <?> {d1}'
question = f'{d1} ?, {f4} ?'
clues = [clue02, clue03, clue04, clue05, clue06, clue07, clue08, clue09, clue10, clue11, clue12, clue13, clue14, clue15, clue16]

# reorder the clues randomly
random.shuffle(clues)

# print the qualities
for i in range(len(qualities)):
    print(f'quality {i+1}: {qualities[i]}')

# print the clues
for i in range(len(clues)):
    print(f'clue {i+1}: {clues[i]}')
print(f'question: {question}')
