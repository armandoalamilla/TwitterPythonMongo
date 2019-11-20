import tweepy
import mongoDB as db
import simplejson as json

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, data):
        #print(data.text)
        db.insertaColeccion(data._json)


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

consumer_key = 'AUpKZNqetVx6r4YoA7J4Hk2xU'
consumer_secret = 'OjhhspAyItBOvE4nFQcTNmfE3CZg1tSnAvjraI4pX9BdIU5G5s'
access_token = '238760734-sEiK8Mht5hpDG0elAIetI3shm5y7GB5av23wdWfP'
access_token_secret = '2IMgpFk7UmzeyInaf6cl4zQx2QgVCAMN3PEoH87dk4TWc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['monterrey, CDMX, ciudad de mexico, guadalajara'])


