import re

pattern = r'colour'
text1 = 'My favourite colour is blue, I love Blue colour'

text2 = re.sub(pattern, 'color', text1, count=1)
print(text2)
text2 = re.sub(pattern, 'color', text1)
print(text2)
