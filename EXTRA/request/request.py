import requests
import json
URL = 'https://www.lasso.cat/restaurant-diccio.html'

text = requests.get(URL)
text  = text.text


print(text)