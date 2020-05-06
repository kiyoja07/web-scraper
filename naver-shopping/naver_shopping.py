import requests
import time
from bs4 import BeautifulSoup

def make_soup(keyword):
    URL = f"https://search.shopping.naver.com/search"
    result = requests.get(f"{URL}/all.nhn?query={keyword}")
    soup = BeautifulSoup(result.text, 'html.parser')
    return soup

def extract_corelation(html):
    """ 연관 검색 정보 가져오기 """
    try:
        title = html.find("div", {"class": "co_relation"}).find("h2").get_text().strip("|")
        values = html.find("div", {"class": "co_relation"}).find_all("a")

        corelations = []
        for value in values:
            value = value.get_text(strip=True).strip("-").strip(" \r").strip("\n")
            corelations.append(value)

        return {"title" : title, "value": corelations}

    except Exception as e:
        return {"title" : "쇼핑연관", "value": "-"}

def extract_filter(html):
    """ 필터 정보 가져오기 """
    try:
        filters = html.find("div", {"id": "_filter"}).find_all("div", {"class": "finder_col"})

        titles = []
        filter_values =[]
        for filter in filters:
            title = filter.find("h3", {"class": "finder_tit"}).find("strong").get_text()
            titles.append(title)
            values = filter.find("ul", {"class": {"finder_tit_list", "finder_list"}}).find_all("li")
            value_list =[]
            for value in values:
                value = value.find("a").get_text(strip=True).strip("-").strip(" \r").strip("\n")
                value_list.append(value)
            filter_values.append(value_list)
        return {"title" : titles, "value": filter_values}
    except Exception as e:
        return {"title" : "필터", "value": None}

def get_search_option(keyword_dict):

    search_option = {}
    keyword_query = keyword_dict["keyword_query"]

    search_option["original_keyword"] = keyword_dict["original_keyword"]

    soup = make_soup(keyword_query)

    corelation = extract_corelation(soup)
    filters = extract_filter(soup)

    if filters["value"]:
        search_option["keyword_query"] = keyword_query
        search_option["search_count"] = keyword_dict["search_count"]
        search_option[corelation["title"]] = corelation["value"]
        for i in range(len(filters["title"])):
            search_option[filters["title"][i]] = filters["value"][i]
        return search_option
    else:
        time.sleep(20)
        return search_option
