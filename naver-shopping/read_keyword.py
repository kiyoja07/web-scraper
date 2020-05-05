import csv

def get_keyword():
    csvfile = open("keywords.csv", mode="r")
    reader = csv.reader(csvfile, delimiter=' ')

    keywords = []
    for row in reader:
        keyword = None
        for word in row:
            if keyword is None:
                keyword = word
            else:
                keyword = keyword + "+" + word
        keywords.append(keyword)
    return keywords