import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

cookies = {
    "over18": "1"
}

res = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(res.text, "html.parser")

articles = soup.find_all("div", class_="title")

for article in articles:
    # Each article be like:
    # <div class="title">
    # <a href="url link">content</a>
    # </div>
    #
    title = article.find("a").text.strip()
    link = article.find("a")
    
    if link:
        url = "https://www.ptt.ccwww.ptt.cc" + link["href"]
    print(f"Title: {title}, URL: {url}")
