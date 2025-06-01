"""
【問題1】ログファイルへの追記処理

以下のコードは、バッチ処理のログを "process.log" に追記する処理です。
ログメッセージは1行ごとに追加される必要があります。

XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX に適切なコードを補完してください。
"""

# log_message = "2025-05-28: バッチ処理完了\n"

# log_file = XXXXXXXXXX("process.log", XXXXXXXXXX)
# log_file.XXXXXXXXXX(log_message)
# log_file.close()

log_message = "2025-06-03: バッチ処理完了\n"
log_path = "process.log"

try:
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(log_message)
    print(f"ログを書き込みました: {log_path}")
except Exception as e:
    print(f"[エラー] ログファイルへの書き込みに失敗しました: {e}")
