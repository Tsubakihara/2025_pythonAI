"""
【問題2】
以下のコードは、関数が呼び出された際に関数名と引数をログ出力するデコレータです。
引数をログに表示する部分が XXXXXXXX になっているので、正しい記述を補完してください。
"""

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"関数 {func.__name__} を呼び出しました。引数: XXXXXXXXX")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def greet(name):
    print(f"こんにちは、{name}さん！")

greet("田中")