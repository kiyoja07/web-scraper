import requests
from bs4 import BeautifulSoup

URL = f"https://search.shopping.naver.com/search"

def get_keyword():
    """ 키워드 리스트에서 키워드 가져오기 """
    keyword = "나이키"
    return keyword

def make_soup(keyword):
    result = requests.get(f"{URL}/all.nhn?query={keyword}")
    soup = BeautifulSoup(result.text, 'html.parser')
    return soup

def extract_corelation(html):
    """ 연관 검색 정보 가져오기 """
    title = html.find("div", {"class": "co_relation"}).find("h2").get_text().strip("|")
    values = html.find("div", {"class": "co_relation"}).find_all("a")

    corelations = []
    for value in values:
        value = value.get_text(strip=True).strip("-").strip(" \r").strip("\n")
        corelations.append(value)

    return {"title" : title, "value": corelations}

def extract_filter(html):
    """ 필터 정보 가져오기 """
    return None


def get_search_option():

    keyword = get_keyword()

    search_option = {}
    search_option["keyword"] = keyword

    soup = make_soup(keyword)

    corelation = extract_corelation(soup)
    filter = extract_filter(soup)


    search_option[corelation["title"]] = corelation["value"]

    print(search_option)

    return None
