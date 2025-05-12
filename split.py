# ユーザーが入力した投稿内容（フォームから送信されたと想定）
raw_input = "Python,AI,機械学習\nこのアプリは不評だ！"

print("=== 元の入力 ===")
print(raw_input)

# --- Step 1: タグの分割（split） ---
tags_line = raw_input.split("\n")[0]  # 1行目を取得（タグ）
tags = tags_line.split(",")           # カンマで分割

# --- Step 2: コメントのNGワード置換 ---
comment_line = raw_input.split("\n")[1]  # 2行目を取得（コメント）
clean_comment = comment_line.XXXXXXXX("不評", "＊＊")

# --- Step 3: タグの結合（join）して表示用文字列に ---
tags_display = " / ".join(tags)

# --- 結果表示 ---
print("\n=== 処理後 ===")
print(f"タグ: {tags_display}")
print(f"コメント: {clean_comment}")
