"""
【Python穴埋め問題】ゲームの持ち物とクエスト管理を作ろう！

■ 問題の目的
この問題では、RPGゲームでよくある「プレイヤーの持ち物」と「クエストの進行状況」を管理するプログラムを作ります。

■ ゲームの設定
- 持ち物（アイテム）はリストで管理します。
- クエストは「タイトル」と「達成状況（True/False）」を持つ辞書で管理します。
- 新しいアイテムを拾ったり、クエストを達成したりする処理を書きます。

■ あなたのミッション
下のプログラムの「XXXXXXXXXX」部分を埋めて、正しく動作するようにしてください。

■ ヒント
- for ○○ in リスト: で1つずつアイテムを取り出せます
- append() を使ってリストにアイテムを追加します
- if ～ else を使ってクエストの表示を切り替えます
- 辞書の値の変更は dict["キー"] = 値 の形で行います
"""

# プレイヤーの持ち物リスト
inventory = ["ポーション", "剣", "盾"]

# クエストの進行状況（未達成: False, 達成済み: True）
quests = [
    {"タイトル": "森の魔物を倒す", "達成": False},
    {"タイトル": "村人に薬を届ける", "達成": True},
]

# 持ち物の表示
print("【持ち物】")
for XXXXXXXXXX in inventory:
    print("-", XXXXXXXXXX)

# クエストの進行状況を表示
print("\n【クエスト】")
for quest in quests:
    status = XXXXXXXXXX if quest["達成"] else XXXXXXXXXX
    print(f"- {quest['タイトル']} [{status}]")

# アイテムを追加
XXXXXXXXXX
print("\n魔法の杖を拾った！")

# クエストの進行更新
quests[0]["XXXXXXXXXX"] = XXXXXXXXXX
print("『森の魔物を倒す』を達成しました！")

# 更新後の状態を再表示
print("\n【更新後の持ち物】")
print(XXXXXXXXXX)

print("\n【更新後のクエスト】")
for quest in quests:
    status = "達成済み" if quest["達成"] else "未達成"
    print(f"- {quest['タイトル']} [{status}]")
