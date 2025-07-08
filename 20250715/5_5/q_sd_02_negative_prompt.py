# ---------------------------------------------
# 問題2: ネガティブプロンプトを用いて画像生成の不要要素を抑制せよ
# 実行方法: python q_sd_02_negative_prompt.py
# negative_prompt パラメータに適切な値を指定し、品質を調整せよ
# ---------------------------------------------

from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to("cuda" if torch.cuda.is_available() else "cpu")

# プロンプトとネガティブプロンプト
prompt = "a beautiful portrait of a woman, 4k, cinematic lighting"
negative_prompt = "XXXXXXXXX"  # 例: "blurry, low quality, distorted"

image = pipe(prompt, negative_prompt=negative_prompt).images[0]
image.save("output_negative.png")
print("ネガティブプロンプト適用画像を生成しました: output_negative.png")
