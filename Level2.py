import collections

res = collections.OrderedDict()
with open('Level2-source.txt') as f:
    for line in f:
        for ch in line:
            if ch in res:
                res[ch] = res[ch] + 1
            else:
                res[ch] = 1
print res