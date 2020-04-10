# n = 12341234
# b1 = (n & 0xff000000) >> 24
# b2 = (n & 0xff0000) >> 16
# b3 = (n & 0xff00) >> 8
# b4 = n & 0xff
# bs = bytes([b1, b2, b3, b4])
# for b in bs:
#     print(b)
# print(bs)

import struct
print("len(hello)=", len(bytes("hello", encoding="utf8")))
print("pack=", struct.pack('>I5s', 12341234, bytes("hello", encoding="utf8")))

print("unpack=", struct.unpack('>I5s', b'\x00\xbcO\xf2hello'))


#  _ _ _ _
# |_|_|_|_|
