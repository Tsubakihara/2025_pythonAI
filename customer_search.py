# 顧客名簿
customers = [
    "Tanaka Hiroshi",
    "Yamada Hanako",
    "Suzuki Taro",
    "Kobayashi Keiko",
    "saito yuki"
]

def search_customer(keyword):
    keyword = keyword.XXXXXXXX()  # 大文字小文字を無視
    results = []

    for name in customers:
        if name.XXXXXXXX().XXXXXXXX(keyword) != -1:  # 部分一致検索
            results.append(name.XXXXXXXXX())  # 見つかった名前を強調（大文字化）

    return results

# --- コマンドラインでのやり取りを想定 ---
if __name__ == "__main__":
    print("=== 顧客検索システム ===")
    while True:
        keyword = input("検索したい名前を入力してください（終了は 'exit'）: ")
        if keyword.lower() == 'exit':
            print("システムを終了します。")
            break

        matched = search_customer(keyword)
        if matched:
            print("\n【検索結果】")
            for name in matched:
                print(" -", name)
        else:
            print("一致する顧客が見つかりませんでした。")
