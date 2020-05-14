import csv

def save_to_csv(i, search_options):
    if i == 0:
        file = open("./export_file/search_options.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(["original_keyword", "keyword_query", "filter_key", "filter_value", "search_count"])
    else:
        file = open("./export_file/search_options.csv", mode="a")
        writer = csv.writer(file)

    original_keyword = search_options.pop("original_keyword")
    keyword_query = search_options.pop("keyword_query")
    search_count = search_options.pop("search_count")

    print(i, original_keyword, "success")

    for key in search_options.keys():
        result = []
        columns = [original_keyword, keyword_query, key, search_options[key], search_count]
        for column in columns:
            result.append(column)
        writer.writerow(result)
    return None

def save_no_result_to_csv(j, search_options):
    if j == 0:
        file = open("./export_file/fail_search_keywords.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(["fail_keyword", "search_count"])
    else:
        file = open("./export_file/fail_search_keywords.csv", mode="a")
        writer = csv.writer(file)

    original_keyword = search_options.pop("original_keyword")
    search_count = search_options.pop("search_count")
    print(original_keyword, "fail")

    result = []
    columns = [original_keyword, search_count]
    for column in columns:
        result.append(column)
    writer.writerow(result)
    return None