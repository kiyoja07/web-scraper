import csv

def get_keyword_query(sentence):
    words = sentence.split(" ")
    for i, word in enumerate(words):
        if i == 0:
            keyword_query = word
        else:
            keyword_query = keyword_query + "+" + word
    return keyword_query

def get_keyword():
    csvfile = open("./import_file/digital_1000.csv", mode="r")
    # csvfile = open("keywords.csv", mode="r")
    reader = csv.reader(csvfile)
    next(reader, None)  # skip the headers

    keywords = []
    for row in reader:
        original_keyword = row[0]
        keyword_query = get_keyword_query(original_keyword)
        search_count = row[2]
        keyword = {"original_keyword": original_keyword, "keyword_query": keyword_query, "search_count": search_count}
        keywords.append(keyword)
    return keywords