import os
import arrow
import tweepy
from dotenv import load_dotenv

load_dotenv()

def sendTweet(request):
    finalMandato = arrow.Arrow(2023, 12, 10)
    comienzoMandato = arrow.Arrow(2019, 12, 10)
    diasQueFaltanDeMandato = ( finalMandato - arrow.now() ).days
    diasTotalesDeMandato = (finalMandato - comienzoMandato).days
    diasQuePasaronDeMandato = (arrow.now() - comienzoMandato).days
    percentageDone = round( ( diasQuePasaronDeMandato / diasTotalesDeMandato ) * 100, 2 )    
    auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET'))
    auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN_KEY'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
    
    api = tweepy.API(auth)
    message = "Faltan " + str( diasQueFaltanDeMandato ) + " días para que termine el gobierno de Alberto Fernández. Ya pasó el " + str( percentageDone ) + "% de su mandato."
    api.update_status(message)
    return 'tweetSent'
