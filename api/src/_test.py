from services import Twitter


twitter = Twitter()

tweets = twitter.get_user_timeline_tweets(id='FernandoPessoa')

print(tweets)