import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ]  | ( )

coreyms.com

984-332-2391
984.303.6818
984*996*9429
800-332-2391
900-332-2391


Mr. Saroj
Mr Deven
Ms Sanju
Mrs. Samjhana
Mr. T

cat 
mat
pat
bat

'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.findall(text_to_search)
for match in matches:
    print(match)
print(text_to_search[1:4])


pattern1 = re.compile(r'start', re.I)
matches1 = pattern1.search(sentence)
print(matches1)

# with open('data.txt', 'r') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)


