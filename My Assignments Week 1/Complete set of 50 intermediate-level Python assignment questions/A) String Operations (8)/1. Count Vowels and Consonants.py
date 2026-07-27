# 1. Count Vowels and Consonants (Unicode-aware)
import unicodedata as ucd

sentence = "He is the number 1 boy in café?"

comp_sentence = ucd.normalize("NFKC", sentence).casefold() # nkfc cz it glues e and ` and casefold helps in safely lower

vowels = ["a","e","i","o","u"]

vowels_count = 0
consonant_count = 0

for i in comp_sentence:
    if i.isalpha():       # if alphabet
        if i in vowels:
            vowels_count += 1
        else:
            consonant_count += 1

print(f"There are {vowels_count} vowels.")
print(f"There are {consonant_count} consonants.")