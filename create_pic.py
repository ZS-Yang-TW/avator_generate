import os
import openai
import requests
from PIL import Image
openai.api_key = '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'

output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# 圖片生成設定
response = openai.Image.create(
  prompt="A cat riding a motorcycle",
  n=1,
  size="256x256"
)
response_urls = response['data']

for i in range(len(response_urls)):
  # 將圖片的網址取出
  image_url = response_urls[i]['url']
  
  # 從url取得圖片
  response = requests.get(image_url, stream=True)
  
  # 利用PIL讀取圖片
  k = Image.open(response.raw)
  
  # 顯示圖片
  # k.show()
  
  output_filename = os.path.join(output_folder, f"user_output_{i}.png")
  
  # 儲存圖片
  k.save(output_filename)