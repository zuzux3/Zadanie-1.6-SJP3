import re

sentence = "Nie lubie w poniedzialki wczesnie wstawac."
a = re.findall(r'\bN\w+', sentence)
b = re.findall(r'\b\w{3}\b', sentence)
c = re.findall(r'\b\w', sentence)

aStr = 'a - string rozpoczynający się od "N"'
bStr = 'wyrazy 3-literowe'
cStr = 'pierwsze litery kolejnych wyrazow'
strEnd = '{}:\n{}: {}\n{}: {}\n{}: {}\n'.format(sentence, aStr, a, bStr, b, cStr, c)

print(strEnd)