# 🔸問題：
# 関数名を文字列で受け取り、該当する関数が定義済みであれば呼び出しを行い、結果を返してください。
# 存在しない関数や呼び出し不可能な値には安全に対応してください。

# 🔸ヒント：
# ・globals()：関数名から関数オブジェクトを取得
# ・callable()：呼び出し可能なオブジェクトかを判定
# ・try / except：安全に関数を実行（例外処理）

def multiply(x: int, y: int) -> int:
    return x * y

def divide(x: int, y: int) -> float:
    return x / y

def safe_invoke(func_name: str, *args) -> object:
    fn = XXXXXXXXXX.get(func_name)             # 関数名から関数を取得
    if XXXXXXXXXX(fn):                         # 呼び出し可能かチェック
        try:
            return XXXXXXXXXX(*args)           # 安全に関数を呼び出し
        except Exception as e:
            return f"実行エラー: {e}"
    return f"{func_name} は呼び出せません"

# 🔸実行例（下記の出力を確認して、穴埋めを完成させましょう）:
print(safe_invoke("multiply", 2, 3))     # 6
print(safe_invoke("divide", 10, 0))      # 実行エラー: division by zero
print(safe_invoke("nonexistent", 1))     # nonexistent は呼び出せません
