# 8. Extract Email-like Tokens
import re

text = 'Please contact me on this email address support@gmail.com or Supports@outlook.com for help'

email = re.findall(r'[^\s]+@[^\s]+',text)

print(f'Emails are:\n{email}')