from naver_shopping import get_search_option as naver_search_option
from save import save_to_csv
from read_keyword import get_keyword

keywords = get_keyword()

for i, keyword in enumerate(keywords):
    search_option = naver_search_option(keyword)
    save_to_csv(i, search_option)




