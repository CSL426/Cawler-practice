import requests
import os
from urllib.parse import urlparse


def download_manga_image(url):
    # 設置headers模擬瀏覽器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.manhuagui.com/',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    try:
        # 發送GET請求
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # 從URL中提取文件名
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # 如果檔名太長，截斷
        if len(filename) > 255:
            filename = filename[-255:]

        # 確保目錄存在
        os.makedirs('downloads', exist_ok=True)

        # 保存圖片
        filepath = os.path.join('downloads', filename)
        with open(filepath, 'wb') as file:
            file.write(response.content)

        print(f"成功下載圖片：{filepath}")
        return filepath

    except requests.RequestException as e:
        print(f"下載失敗：{e}")
        return None


# 使用範例
if __name__ == "__main__":
    # 替換成你的圖片URL
    image_url = "https://eu1.hamreus.com/ps1/y/yf-17169/gydqyd/%E7%AC%AC62%E8%AF%9D/40.jpg.webp?e=1734435828&m=5qmHhZx81ix4PuE02niocA"
    download_manga_image(image_url)
