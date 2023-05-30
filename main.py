import GetOldTweets3 as got
import markovify

maxTweets = 2500
userHandleWanted = str(input("please enter the user's handle:\t"))
#set up criteria for twitter search
tweetCriteria = got.manager.TweetCriteria().setUsername(userHandleWanted)\
  .setMaxTweets(maxTweets)

#need to put all of the retrieved tweets in separate lines of one big string (because we just do for the markov chain generator)
tweetString = ''
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
for tweet in tweets:
  tweetString=tweetString + '\n' + tweet.text

#this builds a markov chain model of word probabilities for the set of tweets we just recovered
text_model = markovify.Text(tweetString)

#this generates a new sentence based on the model and prints it to the console
for i in range(5):
  print("\n"+text_model.make_short_sentence(200))