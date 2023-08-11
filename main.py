from bs4 import BeautifulSoup
import requests
import random

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

movies = response.text
soup = BeautifulSoup(movies, 'html.parser')

movies_list = [movie.getText() for movie in soup.find_all(name='h3', class_='listicleItem_listicle-item__title__hW_Kn')]

#revertendo a lista que se encontra no site da empire do 100 ao 1
for title in reversed(movies_list):
    print(title)

#escolhendo um filme aleatorio da lista e imprimindo
recommendation = movies_list[random.randint(0, len(movies_list))]
print(f'Recomendação do dia: {recommendation}')