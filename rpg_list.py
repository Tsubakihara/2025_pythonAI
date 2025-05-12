# プレイヤーの持ち物リスト
inventory = ["ポーション", "剣", "盾"]

# クエストの進行状況（未達成: False, 達成済み: True）
quests = [
    {"タイトル": "森の魔物を倒す", "達成": False},
    {"タイトル": "村人に薬を届ける", "達成": True},
]

# 持ち物の表示
print("【持ち物】")
for item in inventory:
    print("-", item)

# クエストの進行状況を表示
print("\n【クエスト】")
for quest in quests:
    status = "達成済み" if quest["達成"] else "未達成"
    print(f"- {quest['タイトル']} [{status}]")

# アイテムを追加
inventory.append("魔法の杖")
print("\n魔法の杖を拾った！")

# クエストの進行更新
quests[0]["達成"] = True
print("『森の魔物を倒す』を達成しました！")

# 更新後の状態を再表示
print("\n【更新後の持ち物】")
print(inventory)

print("\n【更新後のクエスト】")
for quest in quests:
    status = "達成済み" if quest["達成"] else "未達成"
    print(f"- {quest['タイトル']} [{status}]")
