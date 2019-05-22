import re

regex = "paupiere"

test_str = open('Tux.svg', 'r').read()
matches = re.findall(regex, test_str)
print(matches)
