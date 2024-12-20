import pandas as pr
import requests as r
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

x = r.get("https://www.indiatoday.in/latest-news")

v = BeautifulSoup(x.text, 'html.parser')
y = v.find_all('a', class_="")
for i in y:
    print(i.text)
    data = i.text


wordcloud = WordCloud(width=800, height=400, background_color='white').generate(data)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.show()