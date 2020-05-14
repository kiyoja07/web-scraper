from naver_shopping import get_search_option as naver_search_option
from save import save_to_csv, save_no_result_to_csv
from read_keyword import get_keyword

keywords = get_keyword()

def run_main():
    success_count = 0
    fail_count = 0
    for keyword in keywords:
        search_option = naver_search_option(keyword)
        if len(search_option) > 2:
            save_to_csv(success_count, search_option)
            success_count =+ 1
        else:
            save_no_result_to_csv(fail_count, search_option)
            fail_count =+ 1
    return None

if __name__ == "__main__":

    run_main()
    # try:
    #     run_main()
    # except Exception as e:
    #     print(e)
    # else:
    #     print('all process was completed')




