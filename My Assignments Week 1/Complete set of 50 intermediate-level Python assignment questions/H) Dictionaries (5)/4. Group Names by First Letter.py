# Group Names by First Letter
name= ['alice','ali','bob','he']
group = {}
for nam in name:
    first = nam[0].upper()
    group.setdefault(first, []).append(nam)
print(group)