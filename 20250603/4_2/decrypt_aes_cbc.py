from Crypto.Cipher import AES
from Crypto.Util.Padding import XXXXXXX  # ← ヒント: パディングを取り除く関数（暗号復号時に使用）

import os

# 暗号鍵と初期化ベクトル（16バイト）
key = b'1234567890abcdef'
iv = b'fedcba0987654321'

# 暗号化ファイルと復号後の出力先
input_path = "XXXXXXXXXXXXXXXXXX"
output_path = input_path.replace(".enc", ".dec.txt")  # ← ヒント: 拡張子を変更して保存

try:
    # 暗号化されたデータを読み込む
    with open(input_path, "rb") as f:
        encrypted_data = f.XXXXXXX()  # ← ヒント: ファイル全体をバイナリで読み取る

    # AES CBC モードで復号
    cipher = AES.new(XXXXXXX, AES.MODE_CBC, iv=iv)  # ← ヒント: 暗号化と同じ16バイトの鍵
    decrypted_data = XXXXXXX(cipher.decrypt(encrypted_data), AES.block_size)  # ← ヒント: パディングを除去して元データに戻す

    # 復号されたデータを保存
    with open(output_path, "wb") as f_dec:
        f_dec.XXXXXXX(decrypted_data)  # ← ヒント: バイナリモードでファイルに書き込む

    print(f"✅ 復号に成功しました: {output_path}")

except FileNotFoundError:
    print(f"❌ エラー: 暗号化ファイルが見つかりません → {input_path}")
except ValueError as e:
    print(f"❌ 復号エラー（おそらく鍵・IV・パディングの問題）: {e}")
except Exception as e:
    print(f"❌ 予期しないエラーが発生しました: {e}")
