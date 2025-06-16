"""
【問題4】
このコードは、引数enabledがTrueの場合のみ実行時間を表示するデコレータです。
時間計測の表示部分の式が XXXXXXXX で隠されています。
開始時刻と終了時刻の差を表示できるように記述を補完してください。
"""

import time

def timer(enabled=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not enabled:
                return func(*args, **kwargs)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"処理時間: {XXXXXXXXX:.4f}秒")
            return result
        return wrapper
    return decorator

@timer(enabled=True)
def work():
    time.sleep(0.5)

work()
