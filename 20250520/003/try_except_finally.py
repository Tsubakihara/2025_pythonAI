# 問題：try / except / finally の基本的な流れ
# リストから指定インデックスの値を取得し、存在しないインデックスでは例外を処理します。

def get_item(lst, index):
    try:
        value = lst[index]
        print("取得成功:", value)
    except XXXXXXXXX as e:
        print("例外発生:", e)
    finally:
        print("終了処理を実行します")

get_item([10, 20, 30], 1)
# 出力:
# 取得成功: 20
# 終了処理を実行します

get_item([10, 20, 30], 5)
# 出力:
# 例外発生: list index out of range
# 終了処理を実行します
