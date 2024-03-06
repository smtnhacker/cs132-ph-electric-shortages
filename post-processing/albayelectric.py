import unicodedata, ast
from sys import stdin

data = []

for line in stdin:
	raw_inp = ast.literal_eval(line).decode()
	clean_inp = unicodedata.normalize('NFKC', raw_inp)

	if "POWER INTERRUPTION" in clean_inp:
		data.append(clean_inp)

print(data)