import re

pattern = r'col'

if re.match(pattern, 'colour is red, I love blue colour'):
    print('Match')

if re.search(pattern, 'colour is red, I love blue colour'):
    print('Found')

print(re.findall(pattern, 'colour is red, I love blue colour'))

# More Search Regular Expression

pattern = r'colour'
text = 'I love Blue colour and Black'

match = re.search(pattern, text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())
