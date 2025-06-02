from typing import Any, Tuple

# record は (文字列, 整数) のタプル
# metadata は Any型、戻り値は None です

def parse_record(record: XXXXXXXXX, metadata: XXXXXXXXX) -> XXXXXXXXX:
 name, age = record
 print(f"Name: {name}, Age: {age}, Extra: {metadata}")
 return XXXXXXXXX

 parse_record(("Tom", 30), {"hobby": "reading"})

# 例:
# parse_record(("Tom", 30), {"hobby": "reading"})
