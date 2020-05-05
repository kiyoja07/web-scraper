import csv

def save_to_csv(i, search_options):
    if i == 0:
        file = open("search_options.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(["original_keyword", "keyword_query", "filter_key", "filter_value", "search_count"])
    else:
        file = open("search_options.csv", mode="a")
        writer = csv.writer(file)

    original = search_options.pop("original")
    keyword = search_options.pop("keyword")
    search_count = search_options.pop("search_count")

    for key in search_options.keys():
        result = []

        result.append(original)
        result.append(keyword)
        result.append(key)
        result.append(search_options[key])
        result.append(search_count)

        writer.writerow(result)
    return None