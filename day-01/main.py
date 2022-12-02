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
    
print(max(sum(inv) for inv in inventory_by_elf(data)))
