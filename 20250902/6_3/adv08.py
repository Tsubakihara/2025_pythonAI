# adv08.py
# ---------------------------------------------
# 問題8: __call__を使ってオブジェクトを関数のように呼べるようにしよう
# ---------------------------------------------
# 【背景】
# ロガーやイベントハンドラなど、オブジェクトを関数のように扱いたいケースがあります。
# __call__メソッドを実装してオブジェクトを関数風に呼べるようにします。
#
# 【今回学ぶポイント】
# ・__call__メソッドの定義
# ・呼び出し時の引数受け取り
# ・オブジェクト内の状態を利用した出力
#
# 【指示】
# ・__call__メソッドの引数を穴埋め
# ・ログメッセージにprefixを付加して出力するロジックを穴埋め
# ・呼び出し時の複数メッセージ処理を追加してください
#

class Logger:
    def __init__(self, prefix):
        self.prefix = prefix
        self.count = 0  # ログ呼び出し回数をカウント

    def __call__(self, XXXXXXXXXXXX):
        # ログメッセージをプリフィックス付きで表示
        print(f"{XXXXXXXXXXXX}: {message}")
        # 呼び出し回数をカウントアップ
        self.count = XXXXXXXXXXXX

    def get_count(self):
        # これまでの呼び出し回数を返す
        return self.count

log = Logger("INFO")
log("System started")
log("An error occurred")
print("ログ呼び出し回数:", log.get_count())
