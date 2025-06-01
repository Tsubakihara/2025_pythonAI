"""
【問題1】Pythonでファイルの中身をAES暗号方式（CBCモード）で暗号化してください。

以下の条件に従って、XXXXXXXXXX の箇所を適切なコードに置き換えてください。

- 対象ファイルは `sample.txt` です（フルパスで指定）。
- 暗号鍵とIV（初期化ベクトル）は16バイトで固定済み。
- 暗号化した内容は `sample.txt.enc` というファイルに出力してください。
- ファイルが存在しない場合はエラーメッセージを表示してください。
- ライブラリ `pycryptodome` を使用してください。
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# 暗号鍵と初期化ベクトル（16バイト）
key = b'1234567890abcdef'
iv = b'fedcba0987654321'

# sample.txt のフルパスを指定（例：Mac環境のパス）
input_path = "XXXXXXXXXX"
output_path = input_path + ".enc"

try:
    # ファイルを開いてデータを読み込む
    with open(XXXXXXXXXX, "rb") as f:
        data = f.read()

    # AES CBC モードで暗号化
    cipher = AES.new(XXXXXXXXXX, AES.MODE_CBC, iv=iv)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    # 暗号化された内容を保存
    with open(XXXXXXXXXX, "wb") as f_enc:
        f_enc.write(encrypted_data)

    print(f"✅ 暗号化に成功しました: {output_path}")

except FileNotFoundError:
    print(f"❌ エラー: 入力ファイルが見つかりません → {input_path}")
except Exception as e:
    print(f"❌ 予期しないエラーが発生しました: {e}")
