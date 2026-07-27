# Validate Tokens; Skip Invalid
raw = '10 abc -5 2.3493 53 xcn'
invalid = 0
total_sum = 0 

for token in raw.split():
    try:
        total_sum += int(token)
    except ValueError:
        invalid += 1
        continue

print(f'Sum:\n{total_sum}\nInvalid Tokens:\n{invalid}')