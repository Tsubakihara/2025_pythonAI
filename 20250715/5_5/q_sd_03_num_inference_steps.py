# ---------------------------------------------
# 問題3: 推論ステップ数を変更し、画像の詳細度を調整せよ
# 実行方法: python q_sd_03_num_inference_steps.py
# num_inference_steps の値を適切に補完し、生成品質を確認せよ
# ◼︎◻︎Google Colabを使用してください◻︎◼︎
# ---------------------------------------------

from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to("cuda" if torch.cuda.is_available() else "cpu")

prompt = "a fantasy landscape with castles and mountains"

# 推論ステップ数を変更
image = pipe(prompt, num_inference_steps=XXXXXXXXX).images[0]  # 例: 25, 50, 100

image.save("output_steps.png")
print("推論ステップ変更による画像を生成しました: output_steps.png")
