from naver_shopping import get_search_option as naver_search_option
from save import save_to_csv, save_no_result_to_csv
from read_keyword import get_keyword

keywords = get_keyword()

def run_main():
    j = 0
    for i, keyword in enumerate(keywords):
        search_option = naver_search_option(keyword)
        if len(search_option) > 1:
            save_to_csv(i, search_option)
        else:
            save_no_result_to_csv(j, search_option)
            j =+ 1
    return None

if __name__ == "__main__":

    try:
        run_main()
    except Exception as e:
        print(e)
    else:
        print('all process was completed')




