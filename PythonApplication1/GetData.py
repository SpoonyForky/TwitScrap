from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#import twitter

#import tweepy

#Variables that contains the user credentials to access Twitter API 
access_token = "760153922136748033-4zEqSejyo6o1TvYQIs3dSi3Hdzmx93x"
access_token_secret = "vkzof7X7wblKeqRb6q4sUIS8UsQcwdNrmqYHm72uswUhi"
consumer_key = "Dsyd03Mnu5PYbmEj9jYPEuzcJ"
consumer_secret = "mYiBzM1N5lfKF17HyEZ5OaKIpFYmq1RQDiXIjrx41AdHc2etT1"

class StdOutListener(StreamListener):
    
    
    def on_data(self,data):
        outfile = open("data.txt","a")
        print (data, file=outfile)
        outfile.closed

        return True

    def on_error(self,status):
        print (status, file = outErrorfile)



if __name__ == "__main__":
    #Data file
   
    #Error file
    outErrorfile = open ("error.txt","a")
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth,l)
    stream.filter(track=['python','javascript','ruby'])
  
   
   