"""
【問題3】
以下のコードは、渡された引数がすべて整数（int）型であることを検証するデコレータです。
整数以外が渡された場合、例外をスローします。
型チェック部分が XXXXXXXX になっていますので、正しい条件を補完してください。
"""

def check_int_args(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not XXXXXXXXX:
                raise ValueError("すべての引数はint型である必要があります")
        return func(*args, **kwargs)
    return wrapper

@check_int_args
def add(a, b):
    return a + b

print(add(3, 5))
# print(add(3, "hello"))  # エラーになる
