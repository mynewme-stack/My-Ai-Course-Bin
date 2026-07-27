# 1. Unique Words in a Text
import re 
text= "Apple! banana, APPLE... banana, grape."
word = re.findall(r"\w+", text.casefold())
unique = set(word)
print(unique)