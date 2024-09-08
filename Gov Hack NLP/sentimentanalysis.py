from transformers import pipeline
sentiment_analyzer = pipeline('sentiment-analysis')

tweet_sentiments = [sentiment_analyzer(tweet) for tweet in tweets]
article_sentiments = [sentiment_analyzer(article) for article in articles]
