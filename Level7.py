import Image

im = Image.open('oxygen-L7.png')
im_pixels = list(im.getdata())
res_comment = []
for i in im_pixels[::7]:
    res_comment.append(chr(i[0]))
res = ''.join(res_comment[-44:-1])
for i in res.split(','):
    print chr(int(i)),