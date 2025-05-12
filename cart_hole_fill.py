"""
【Python穴埋め問題】業務風：ショッピングカート管理システム

■ 概要
このプログラムは、商品を追加・削除できる「カート管理アプリ」です。

■ ミッション
「XXXXXXXX」の部分に正しいコードを記述して、
カートが正しく動作するようにしてください。
"""

# カートの初期状態
cart = []

# カートの中身を表示する関数
def show_cart():
    print("\n【現在のカート】")
    if cart:
        for idx, item in enumerate(cart):
            print(f"{idx + 1}. {item}")
    else:
        print("カートは空です。")

while True:
    print("\n--- カート管理メニュー ---")
    print("1: 商品を追加 (append)")
    print("2: 商品を複数追加 (extend)")
    print("3: 指定位置に商品を追加 (insert)")
    print("4: 商品を削除 (remove)")
    print("5: 最後の商品を取り出して削除 (pop)")
    print("6: カートを空にする (clear)")
    print("7: カートを見る")
    print("0: 終了")

    choice = input("操作を選んでください: ")

    if choice == "1":
        item = input("追加する商品名を入力してください: ")
        XXXXXXXXXX
        print(f"{item} をカートに追加しました。")

    elif choice == "2":
        items = input("カンマ区切りで複数商品を入力してください（例: 商品A,商品B）: ")
        item_list = [i.strip() for i in items.split(",")]
        XXXXXXXXXX
        print("商品をまとめてカートに追加しました。")

    elif choice == "3":
        item = input("追加する商品名を入力してください: ")
        index = int(input("何番目に追加しますか？（先頭は 0）: "))
        if 0 <= index <= len(cart):
            XXXXXXXXXX
            print(f"{item} を {index} 番目に追加しました。")
        else:
            print("無効な位置です。")

    elif choice == "4":
        item = input("削除する商品名を入力してください: ")
        if item in cart:
            XXXXXXXXXX
            print(f"{item} を削除しました。")
        else:
            print("その商品はカートにありません。")

    elif choice == "5":
        if cart:
            XXXXXXXXXX
            print(f"{removed} をカートから取り出しました。")
        else:
            print("カートは空です。")

    elif choice == "6":
        XXXXXXXXXX
        print("カートを空にしました。")

    elif choice == "7":
        show_cart()

    elif choice == "0":
        print("終了します。")
        break

    else:
        print("無効な選択です。もう一度選んでください。")
