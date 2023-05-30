#import the python module that will retrieve tweets for us
import GetOldTweets3 as got

#define search terms to determine what we return from twitter
tweetCriteria = got.manager.TweetCriteria()\
  .setUsername("kanyewest")\
  .setMaxTweets(100)

tweetText=''
maxRetweets = 0

#print the tweet we just searched for
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
for tweet in tweets:
  if tweet.retweets>maxRetweets:
    tweetText = tweet.text
    maxRetweets = tweet.retweets

print(tweetText)
print(maxRetweets)