#import bibliotek
import requests
from bs4 import BeautifulSoup

#adres URL strony z opiniami
url = "https://www.ceneo.pl/76891701#tab=reviews"

#pobranie kodu HTML strony z adresu URL
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')

#wybranie z kodu strony fragmentów odpowiadających poszczególnym opiniom
opinions = page_tree.select("li.review-box")

#ekstrakcja składowyh dla pojedynczej opinii z listy
opinion = opinions.pop() 
opinion_id = opinion["data-entry-id"]
print(opinion_id)
author = opinion.select('div.reviewer-name-line').pop().string
recomendation = opinion.select('div.product-review-summary > em').pop().string
stars = opinion.select('span.review-score-count').pop().string
purchased = opinion.select('div.product-review-pz').pop().string
useful = opinion.select('button.vote-yes').pop()["data-total-vote"]
useless = opinion.select('button.vote-no').pop()["data-total-vote"]
content = opinion.select('p.product-review-body').pop().get_text()

# - data wystawienia: span.review-time > time["datetime"] - pierwsze wyystąpienie
# - data zakupu: span.review-time > time["datetime"] - drugie wyystąpienie

# - wady: div.cons-cell > ul
# - zalety: div.pros-cell > ul
