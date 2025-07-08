# ---------------------------------------------
# 問題1: Stable Diffusion を使用し、指定プロンプトに基づいて画像を生成せよ
# 実行方法: python q_sd_01_prompt.py
# Hugging Face の diffusers ライブラリを使用すること
# ---------------------------------------------

from diffusers import StableDiffusionPipeline
import torch

# モデル読み込み（初回はDLが必要）
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# プロンプト指定
prompt = "XXXXXXXXX"  # 生成したい内容を記述せよ（例: "a futuristic city at sunset"）

# 画像生成
image = pipe(prompt).images[0]

# 保存
image.save("output_prompt.png")
print("画像を生成しました: output_prompt.png")
