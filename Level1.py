input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
ans = ''
for ch in input:
    if ch == 'y':
        ch = 'a'
    elif ch == 'Y':
        ch = 'A'
    elif ch == 'z':
        ch = 'b'
    elif ch == 'Z':
        ch = 'B'
    elif ch.isalpha():
        ch = chr(ord(ch)+2)
    ans = ans + ch
print ans