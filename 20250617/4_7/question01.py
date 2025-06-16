"""
【問題1】
以下のコードは、関数の実行時間を計測するデコレータを作成するものです。
デコレータ `timer` の戻り値の部分が XXXXXXXX で隠されています。
デコレータとして機能するように、適切なコードを埋めてください。
"""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"実行時間: {end - start:.4f}秒")
        return result
    return XXXXXXXXX

@timer
def slow_func():
    time.sleep(1)

slow_func()