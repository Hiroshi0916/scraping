import requests
from bs4 import BeautifulSoup
import os

# スクレイピングするURLを指定

base_url ='https://books.toscrape.com/'
# category_url='catalogue/category/books/mystery_3/index.html'
category_url='catalogue/category/books/sequential-art_5/index.html'

full_url=base_url+category_url

# requestsを使ってWebページを取得
# response = requests.get(base_url)
response = requests.get(full_url)
response.raise_for_status()

# BeautifulSoupを使ってHTMLを解析
soup = BeautifulSoup(response.text, 'html.parser')

# imgタグを取得
img_tags = soup.find_all('img')

# 画像のURLを取得
img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

# URLからフォルダ名として使用する部分を取得
folder_name = full_url.split('/')[-2]

# フォルダが存在しない場合、フォルダを作成
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 画像をダウンロードして保存
for img_url in img_urls:
    # 相対URLを絶対URLに変換
    # full_img_url = os.path.join(base_url, img_url)
    full_img_url = base_url + img_url.lstrip('/')

    img_response = requests.get(full_img_url)
    img_response.raise_for_status()

    # ファイル名を生成
    filename = os.path.join(folder_name, os.path.basename(img_url))
    
    # 画像を保存
    with open(filename, 'wb') as f:
        f.write(img_response.content)

    print(f'{filename} を保存しました。')
