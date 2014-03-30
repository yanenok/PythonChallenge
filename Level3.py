import re

with open('Level3-source.txt') as f:
    for line in f:
        match = re.search('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', line)
        if match:
            print line[match.start()+4]