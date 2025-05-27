# data はバイト列、戻り値は真偽値です。

def is_valid(data: XXXXXXXXX) -> XXXXXXXXX:
 return data.startswith(b"\x89")

# 例:
# print(is_valid(b"\x89PNG")) # True