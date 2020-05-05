import requests
from bs4 import BeautifulSoup

URL = f"https://search.shopping.naver.com/search"

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

    filters = html.find("div", {"id": "_filter"}).find_all("div", {"class": "finder_col"})

    titles = []
    filter_values =[]
    for filter in filters:
        title = filter.find("h3", {"class": "finder_tit"}).find("strong").get_text()
        titles.append(title)
        values = filter.find("ul", {"class": {"finder_tit_list", "finder_list"}}).find_all("li")
        each_values =[]
        for value in values:
            value = value.find("a").get_text(strip=True).strip("-").strip(" \r").strip("\n")
            each_values.append(value)
        filter_values.append(each_values)

    return {"title" : titles, "value": filter_values}


def get_search_option(keyword_dict):

    search_option = {}

    keyword = keyword_dict["keyword"]
    search_option["keyword"] = keyword
    search_option["original"] = keyword_dict["original"]
    search_option["search_count"] = keyword_dict["search_count"]

    soup = make_soup(keyword)

    corelation = extract_corelation(soup)

    search_option[corelation["title"]] = corelation["value"]

    filters = extract_filter(soup)
    for i in range(len(filters["title"])):
        search_option[filters["title"][i]] = filters["value"][i]

    return search_option
