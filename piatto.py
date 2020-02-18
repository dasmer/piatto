import sys
import csv
import io

from bs4 import BeautifulSoup

css = open('style.css').read()
csv = csv.DictReader(io.open(sys.argv[1], "r", encoding = "utf-8-sig"))

categories = []
rawItems = []
for item in csv:
    rawItems.append(item)
    category = item["item_category"]
    if category not in categories:
        categories.append(category)


list = dict()
for category in categories:
    categoryItems = []
    for item in rawItems:
        itemCategory = item["item_category"]
        if category == itemCategory:
            categoryItems.append(item)
    list[category] = categoryItems


html = "<style>" + css + "</style>"
html += "<div class=\"menu-body\">"

for category in categories:
    items = list[category]

    html+= "<div class=\"menu-section\"><h2 class=\"menu-section-title\">" + category + "</h2>"

    for item in items:
        description = item["item_description"]
        if item["item_vegan"] == "TRUE":
            description += "(Vegan)"
        if item["item_glutenfree"] == "TRUE":
            description += "(Gluten-Free)"


        html += "<div class=\"menu-item\">"

        html += "<div class=\"menu-item-name\">" + item["item_name"] + "</div>"
        html += "<div class=\"menu-item-price\">$" + item["item_price"] + "</div>"
        html += "<div class=\"menu-item-description\">" + description + "</div>"

        html += "</div>"


    html += "</div>"

html += "</div>"

soup = BeautifulSoup(html, "html.parser")

html = soup.prettify()


html_file = open(sys.argv[2], "w")
html_file.write(html)
html_file.close()
