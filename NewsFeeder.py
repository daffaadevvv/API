from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    
    feed = feedparser.parse( rss_url ) 
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])
        headlines.append(newsitem['link'])
    
    return headlines

@app.route('/')
def index():

    # A list to hold all headlines
    allheadlines = []
    
    # List of RSS feeds that we will fetch and combine
    newsurls = {
        'rtnews':           'https://www.rt.com/rss/',
        'googlenews':       'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US'
    }
    
    # Iterate over the feed urls
    for key,url in newsurls.items():
        # Call getHeadlines() and combine the returned headlines with allheadlines
        allheadlines.extend( getHeadlines( url ) )

    print(allheadlines)

    return jsonify(allheadlines)


if __name__ == '__main__':
    app.run(debug = True)
