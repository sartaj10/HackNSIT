from flask import Flask, render_template, request, redirect, json, url_for
import tweepy

app = Flask(__name__)

# Home Page
@app.route('/')
def main():
	return render_template('index.html')

@app.route('/twitter')
def showtweets():
    consumer_key        = '0myASUiii6fCxbpTHyXNryP9k'
    consumer_secret     = 'GYIqctWSh6NvGWexo5QG8gTLWHMGsOi1mui5SuxSGwu7JeH1WZ'
    access_token        = '1259588774-i76RdUMP8r7F9oPzqLwJwzdvwgmATEXMJkMEVDz'
    access_token_secret = 'zOyrLduYcEyZvPjuohR4VU0HeGDFSDYLyEfXmLABIJ1ny'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print tweet.text.encode('utf8')
        
    return render_template('tweets.html', tweets = public_tweets)

# App Run
if __name__ == '__main__':
	app.run(debug=True, port = 5002)
