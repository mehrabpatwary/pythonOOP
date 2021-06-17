import re

pattern = r'^colo..r$'

if re.match(pattern, 'colouhr'):
    print("Matched1")
pattern = r"(ab)*"  # Zero or More ab

if re.match(pattern, 'colouhr'):
    print("Matched2")

pattern = r"a+"  # One or More a

if re.match(pattern, 'abandon'):
    print("Matched3")

pattern = r"a+b"  # One or More a

if re.match(pattern, 'abandon'):
    print("Matched4")

pattern = r"ice(-)?cream"  # Zero or One -

if re.match(pattern, 'ice-cream'):
    print("Matched5")

pattern = r"a{1,3}$"  # 1/2/3 - a

if re.match(pattern, 'aaa'):
    print("Matched6")

pattern = r"[A-Z][a-z][0-9]"  # Set of character
# pattern = r"[aeiou]"  # Set of character

if re.match(pattern, 'Fs6fjyjgrt'):
    print("Matched7")
