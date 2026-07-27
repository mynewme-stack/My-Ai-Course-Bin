# 5. Check Balanced Brackets with Types ()[]{}
text = '{[()]}'
stack = []
pairs = {')':'(',']':'[','}':'{'}
valid = True
for i in text:
    if i in '([{':
        stack.append(i)
    elif i in ')]}':
        if not stack or stack.pop() != pairs[i]:
            valid=False
            break
print(valid and not stack)