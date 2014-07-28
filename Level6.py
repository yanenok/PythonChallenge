import zipfile

with zipfile.ZipFile('channel.zip', 'r') as zf:
    name = '90052.txt'
    res = []
    while True:
        text = zf.read(name)
        res.append(zf.getinfo(name).comment)
        if text.startswith('Next nothing is '):
            num = int(text[16:])
            name = str(num)+'.txt'
        else:
            break
    print ''.join(res)