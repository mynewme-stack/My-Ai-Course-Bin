# 2. Title Case with Minor Words Exempt

import string as st       # access predefined constants

sentence = "a wild dog was not barking near area: 512."
minor = {"a","an","the","near","here","by","us"}

word_list = sentence.split()     # split every word
final = []

for index in range(len(word_list)):      
    raw = word_list[index]
    clean = raw.strip(st.punctuation)                 # separate punctuations within strings
    if index == 0 or index == len(word_list) - 1 or clean.lower() not in minor:
        clean = clean.capitalize()
    else:
        clean = clean.lower()
    fix = raw.replace(raw.strip(st.punctuation), clean)
    final.append(fix)
out = " ".join(final)

print(out)