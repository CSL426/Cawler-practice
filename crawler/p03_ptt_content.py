from pathlib import Path
import requests
from bs4 import BeautifulSoup
from p03_ptt_content_getstring import get_article_string

write_dir = Path("ptt_article")
# Create folder
write_dir.mkdir(exist_ok=True)
# write_file = write_dir / "ppt_content.txt"

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
cookies = {
    "over18": "1"
}

res = requests.get(
    url,
    headers=headers,
    cookies=cookies
)
soup = BeautifulSoup(res.text, "html.parser")

articles = soup.find_all("div", class_="title")

for article in articles:
    # Each ariticle be like:
    # <div class="title">
    # <a href="url link">content</a>
    # </div>
    title = article.find("a").text.strip()
    link = article.find("a")

    if link:
        article_url = "https://www.ptt.cc" + link["href"]
    # print(f"Title: {title}, URL: {article_url}")

    # Get article content "string"
    article_string = get_article_string(article_url)

    # write
    for replace_word in ["/", "?", "@", "#", "*", ":"]:
        title = title.replace(replace_word, "")
    title = title + ".txt"
    write_file = write_dir / title

    with write_file.open(mode="w", encoding="UTF-8") as f:
        f.write(article_string)
        f.write("---------------------------------------------------------------------------")

print("finish!")
