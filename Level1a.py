def translate(str):
    ans = ''
    for ch in str:
        if ch == 'y':
            ch = 'a'
        elif ch == 'z':
            ch = 'b'
        elif ch.isalpha():
            ch = chr(ord(ch)+2)
        ans = ans + ch
    return ans

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print translate(input)
print translate('map')