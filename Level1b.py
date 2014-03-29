from string import ascii_lowercase, maketrans, translate

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
map = maketrans(ascii_lowercase, ascii_lowercase[2:] + ascii_lowercase[:2])
print input.translate(map)
print 'map'.translate(map)