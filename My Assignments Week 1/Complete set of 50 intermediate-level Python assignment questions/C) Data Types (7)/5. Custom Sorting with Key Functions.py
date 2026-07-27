# 5. Custom Sorting with Key Functions
mix = ['10','she','7','ui']
mix.sort(key=lambda s : (not s.isdigit(),s.casefold()))
print(mix)