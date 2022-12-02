# coding: utf-8
with open("input.txt", encoding="utf-8") as f:
    data = f.readlines()
    
def inventory_by_elf(inventory):
    elf = []
    for entry in inventory:
        if entry == '\n':
            yield elf
            elf = []
        else:
            elf.append(int(entry))
    yield elf

elves = list(sum(inv) for inv in inventory_by_elf(data))
elves.sort()
elves = list(reversed(elves))
top_three = elves[:3]

    
print(sum(top_three))
