import csv

def get_keyword():
    csvfile = open("keywords.csv", mode="r")
    reader = csv.reader(csvfile)
    next(reader, None)  # skip the headers

    keywords = []
    for row in reader:
        original = row[0]
        original_word_list = original.split(" ")
        for i, word in enumerate(original_word_list):
            if i == 0:
                words = word
            else:
                words = words + "+" + word
        search_count = row[1]
        result = {"original": original, "keyword": words, "search_count": search_count}
        keywords.append(result)
    return keywords