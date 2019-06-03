import string
import re

with open('input.txt','r') as f:
    contents = f.read()
    f.close()


content2 = re.findall(r'\"(\w+)\"',contents)

print(content2)
