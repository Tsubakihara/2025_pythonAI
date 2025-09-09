# ファイル名: item04.py
# ヒント: 翻訳辞書クラスを作り、キーで翻訳を取得・更新できるようにする。

class Translation:
    def __init__(self):
        self.words = {"apple": "りんご", "car": "車"}

    def XXXXXXXXXXX(self, word):  # get
        return self.words.get(word, "未登録")

    def XXXXXXXXXXX(self, word, meaning):  # set
        self.words[word] = meaning

t = Translation()
print(t["apple"])     # 期待値: りんご
t["car"] = "自動車"
print(t["car"])       # 期待値: 自動車
print(t["train"])     # 期待値: 未登録
