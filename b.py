from bs4 import BeautifulSoup
import requests
response = requests.get("https://example.com/api/products")
data = response.text
soup = BeautifulSoup(data)
for link in soup.find_all('rating' > 4):
    print (link.get('product'))
