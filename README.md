# Opis kodu

Do pobierania danych stworzona została metoda fetch_url(), która przesyła od zawartość strony od serwera do przeglądarki na podsatwie dokumentu HTML z danymi.

Nastepnie za pomocą pakietu BeautifulSoup szukamu elementu stron, w tym przypadku klas, które zawierają interesujące nas dane, takie jak tytuł filmu, czas trwania oraz rok. Na podstawie zebranych danych twórzymy listę, która przechowuje zescrappowane dane (lista list). Do niej dorzucamy listę reżyserów, która została pobrana z osobnego elementu strony. Na koniec wszystko eksportowane jest do pliku csv.
