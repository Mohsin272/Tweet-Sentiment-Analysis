import tweepy
from textblob import TextBlob

#API KEYS
access_token='947914504024809472-hc3wK53BvMXd8ta6hA97iVATgvyc5Yg'
access_secret='6Yboid7VjbQNAbgciv2X04R6JyLVDAE2OR1yni4gMCKMV'
api_key='zTALD7Y7admASLghGZbFL0nZF'
api_secret='hIK0bkFFpdWIxVjnmffcTdTyS6BSeUuNYDhgk8yKlDjqFsuoCB'

#authenticating api with keys
auth=tweepy.OAuthHandler(consumer_key=api_key,consumer_secret=api_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)

negative=0
positive=0
neutral=0

choice=input('Enter a search term: ')
num_of_tweets=int(input('Enter how many tweets to be generated: '))
tweets=tweepy.Cursor(api.search,q=choice,lang='en',wait_on_rate_limit=True,wait_on_rate_limit_notify=True).items(num_of_tweets)#querying the api with user hashtag
#rate limit waits for time to pass instead of crashing program,wait time notify how long until i can use api again

for tweet in tweets:

	final_text=tweet.text.replace('RT','')##removing RT from start of string
	if final_text.startswith(' @'):#finds text starting with blank space and @
		position=final_text.index(':')#finds colon
		final_text=final_text[position+2:]#text starts from after the colon was found

	if final_text.startswith('@'):#if it start with only @ sign
		position=final_text.index(' ')#find the whitepsace
		final_text=final_text[position+2:]#text starts 2 spaces after whitespace found

	nature=TextBlob(final_text)
	tweet_polarity=nature.polarity
	if (tweet_polarity==0.00):#if its netral add 1 to the nuetral number of tweets
		neutral+=1

	elif(tweet_polarity>0.00):#if its greater than 0 (positive) then add 1 to the num of pos tweets
		positive+=1

	elif(tweet_polarity<0.00):#if its less than 0 (neg) then add 1 to the num of neg tweets
		negative+=1
#calculate percentage
positive_percent=(positive/num_of_tweets)*100
negative_percent=(negative/num_of_tweets)*100
neutral_percent=(neutral/num_of_tweets)*100
#int(positive_percent)
#int(negative_percent)
#int(neutral_percent)
print(f'The number of positive tweets = {positive} {positive_percent}% ')
print(f'The number of negative tweets = {negative} {negative_percent}%')
print(f'The number of neutral tweets = {neutral} {neutral_percent}%')


