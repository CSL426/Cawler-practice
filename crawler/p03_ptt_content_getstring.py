import requests
from bs4 import BeautifulSoup

# article_url = "https://www.ptt.cc/bbs/Gossiping/M.1731081383.A.48A.html"


def get_article_string(article_url: str) -> str:

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    cookies = {
        "over18": "1",
    }
    res_article = requests.get(
        article_url,
        headers=headers,
        cookies=cookies,
    )

    soup_article = BeautifulSoup(res_article.text, "html.parser")
    soup_article_content = soup_article.select_one(
        'div[id="main-content"]',
    )

    extract_attr_list = [
        ".article-metaline",
        ".push",
        ".richcontent",
        ".article-metaline-right",
        ".f2",
    ]
    for attr in extract_attr_list:
        for tag in soup_article_content.select(attr):
            tag.extract()

    return soup_article_content.text

if __name__ == "__main__":
    article_url = "https://www.ptt.cc/bbs/Gossiping/M.1731081383.A.48A.html"
    print(get_article_string(article_url))
