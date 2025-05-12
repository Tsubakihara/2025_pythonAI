#1.	顧客名簿（リスト形式）に複数の名前が登録されている。
#2.	ユーザーが名前の一部を入力すると、それを部分一致で検索する。
#3.	検索では大文字・小文字の区別をしない。
#4.	該当する顧客がいた場合、大文字に変換して表示する。
#5.	ユーザーが exit と入力するまで繰り返す。
#6.	一致しなかった場合は「一致する顧客が見つかりませんでした」と表示する。



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
            print("XXXXXXXXXX")
