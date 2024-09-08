import requests

url = 'https://newsapi.org/v2/everything?q=wellbeing&from=2023-01-01&sortBy=popularity&apiKey=your_api_key'
response = requests.get(url)
data = response.json()
articles = data['articles']
