# Example puzzle: herbalists (possibly unsolvable)

## Qualities
- names: 
    - a1: Antonius
    - a2: Domingo
    - a3: Flavian
    - a4: Horacio
    - a5: Lucius

- herbs: 
    - b1: mandrake root
    - b2: cinquefoil
    - b3: rosemary
    - b4: juniper berries
    - b5: mistletoe
           
- moon phase: 
    - c1: new
    - c2: first quarter
    - c3: full
    - c4: third quarter
    - c5: waning crescent
- amount: 
    - d1: a bit
    - d2: some
    - d3: standard
    - d4: a lot
    - d5: pile

## Clues
1. mandrake root was collected in a standard amount in the third quarter.
2. rosemary was collected on a new moon in the maximum possible amount, but not by domingo.
3. antonius and horacio were working on either a full moon or the third quarter.
4. the juniper berries were collected on the moon's first quarter.
5. no one was collecting mistletoe on the two last phases of the moon.
6. horacio harvested the smallest possible amount of herbs on a full moon.
7. three herbalists - the one who collected only some herbs, another who collected mandrake root, and flavian - were working on first and third quarters of the moon, and also on the waning crescent.

## Abstraction
- quality A: a1, ..., a5 -> names
- quality B: b1, ..., b5 -> herbs
- quality C: c1, ..., c5 -> moon phase
- quality D: d1, ..., d5 -> amount

## Abstracted clues
1. b1 & d3 & c4
2. (b3 & c1 & d5) !& a2
3. (a1 & c3, a4 & c4) or (a1 & c4, a4 & c3)  //  (a1, a4) &? (c3, c4)
4. b4 & c2
5. b5 !& c4, b5 !& c5
6. a4 & d1 & c3
7. (d2, b1, a3) &? (c2, c4, c5)

# Clue abstraction notation
- A & B : A belongs to B = B belongs to A
- A !& B : A and B do not belong together
- (A, B) &? (C, D) : A and B belong to C and D, but the exact relations are unknown, short for (A & C, B & D) or (A & D, B & C), from this it follows that A !& B, C !& D

# Additional notation for puzzles with an ordered quality
- A < B : A is directly left of B
- A > B : A is directly right of B
- A << B : A is left of B, but not necessarily right next to B
- A >> B : A is right of B, but not necessarily right next to B
- A <?> B : A and B are directly next to each other
