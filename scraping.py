import requests
from bs4 import BeautifulSoup
import os

# スクレイピングするURLを指定
url ='https://books.toscrape.com/'
# img_url = "media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"
# full_img_url = base_url + img_url

# requestsを使ってWebページを取得
response = requests.get(url)

response.raise_for_status()

# BeautifulSoupを使ってHTMLを解析
soup = BeautifulSoup(response.text, 'html.parser')

# imgタグを取得
img_tags = soup.find_all('img')

# 画像のURLを取得
img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

# 画像をダウンロードして保存
for img_url in img_urls:
    # 相対URLを絶対URLに変換
    full_img_url = os.path.join(url, img_url)
    
    img_response = requests.get(full_img_url)
    img_response.raise_for_status()

    # ファイル名を生成
    filename = os.path.join(".", os.path.basename(img_url))
    
    # 画像を保存
    with open(filename, 'wb') as f:
        f.write(img_response.content)

    print(f'{filename} を保存しました。')
