from itertools import chain
from string import ascii_lowercase, ascii_uppercase

def into_rucksacks(contents):
    middle = len(contents) // 2
    return (contents[:middle], contents[middle:])

def find_common_item(xs, ys):
    for x in xs:
        for y in ys:
            if x == y:
                return x

# dictionary mapping a letter to its assigned priority
priority_by_letter = dict(map(reversed, enumerate(chain(ascii_lowercase, ascii_uppercase), start=1)))

with open("input.txt") as f:
    data = f.readlines()

rucksacks = map(into_rucksacks, data)
common_items = [find_common_item(xs, ys) for (xs, ys) in rucksacks]
priorities = map(priority_by_letter.get, common_items)
priority_sum = sum(priorities)
print(priority_sum)
