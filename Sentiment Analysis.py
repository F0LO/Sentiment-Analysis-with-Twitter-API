#import the python module that will retrieve tweets for us
import GetOldTweets3 as got
import string
from random import *

wantedUserHandle = input("please enter the user's handle:\t")
wantedAmount = int(input("how many tweets do you want:\t"))
#function to read in text file
def readWordFile(filename):
  wordFile = open(filename,"r")
  wordsIn = wordFile.read().split('\n')
  wordFile.close()
  return wordsIn

#need to clean up words to compare them to our lists by removing punctuation and capital letters
def clean(inWord):
  outWord = inWord.lower().translate(str.maketrans('', '', string.punctuation))
  return outWord
#read in lists of positive and negative terms
positiveWordList = readWordFile('positive-words.txt')
negativeWordList = readWordFile('negative-words.txt')

tweetCriteria = got.manager.TweetCriteria().setUsername(wantedUserHandle)\
   .setMaxTweets(wantedAmount)

#select the first tweet (in position 0 - as specified in the square brackets at the end) and print it
def checkSentiment(Tweeted):
  count = 0
  for words in Tweeted:
    if words in positiveWordList:
      count += 1
    elif words in negativeWordList:
      count -= 1
  #if count >-1:
  #  print("this is a positive tweet")
  #  print("sentiment score:", count)
  #elif count == 0:
  #  print("this has no skew")
  #else:
  #  print("this guy is mean")
  #  print("sentiment score:", count)
  return count
loop_count=0

while not loop_count > wantedAmount:
  tweet = got.manager.TweetManager.getTweets(tweetCriteria)[loop_count-1]
   # SPACE!!!!!

#split = the tweet we retrieved into individual words (create a list of strings by dividing the tweet at every space)
  testTweet = tweet.text.split()
  #print("Original tweet:")
  #print(tweet.text)


  overall_sentiment = checkSentiment(testTweet)
  loop_count+=1
if overall_sentiment > -1:
  print("\nMost of",wantedUserHandle + "'s tweets are positive")
else:
  print("\n"+wantedUserHandle,"is a mainly negative person on twitter")
#.setMaxTweets(100)\