
# CeneoScrapper
# Etap 1 - pobranie pojedynczeej opinii 
- opinia li.review-box
- identyfikator li.review-box["data.entry-id"]
- autor div.reviever-name-line
- rekomendacja div.product-reviever-summary > em
- liczba gwiazdek span.review-score-count
- czy potwierdzona zakupem div.product.review-pz
- data wystawienia span.review-time > time
["datetime"] - pierwsze wystapienie
- data zakupu span.review-time > time
["datetime"] - drugie wystapienie
- przydatna button.votes-yes ["data-total-votes"]
- nieprzydatna button.votes-no ["data-total-votes"]
- treść p.product-review-body
- wady div.cons-cell > cons
- zalety div.pros-cell > pros
## Etap 2 - pobranie wszystkich opinii z pojedynczej strony
- zapis składowych opinii do złożonej struktury danych
## Etap 3 - pobranie wszystkich opinii o pojedynczym produkcie
- sposób przechodzenia po kolejnych stronach z opiniami
- eksport opinii do pliku (.csv lub .xlsx lub .json)
## Etap 4 -  
- eliminacja powtarzających się fragmentów kodu 
- transformacja danych (typ danych, czyszczenie danych)
## Etap 5 - analiza pobranych danych
- zapis pobranych danych do obiektu dataframe (ramka danych)
- wykonanie prostych obliczeń na danych
- wykonanie prostych wykresów
-(blad w linii 59 opinions = page_tree.select("li.review-box") > opinions = page_tree.select("li.js_product-review"))
## Etap 6 - interfejs webowy aplikacji (framerwork Flask)
- zainstalowanie i uruchomienie Flask'a
- routing (nawigowanie po stronach serwisu)
- widoki (Jinja)
