"""
【問題5】
このデコレータは、関数を指定した回数だけ繰り返して実行します。
繰り返し処理を行うループの対象が XXXXXXXX で隠されています。
n回ループを実行するために適切な記述を補ってください。
"""

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in XXXXXXXXX:
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
