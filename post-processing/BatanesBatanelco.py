import unicodedata, ast, re, emoji
from sys import stdin

data = []

for line in stdin:
    raw_inp = ast.literal_eval(line).decode()
    clean_inp = unicodedata.normalize('NFKC', raw_inp)
    clean_inp = emoji.replace_emoji(clean_inp, replace='')
    
    if "power interruption" in clean_inp.lower():
        data.append(clean_inp)

print(data)