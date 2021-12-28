import datetime
from feedgen.feed import FeedGenerator

import os
from flask import Flask, Response, request
from flask_mongoengine import MongoEngine
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': 'webapp'
}
db = MongoEngine()
db.init_app(app)
class Movie(db.Document):
    title = db.StringField(max_length=60)
    description = db.StringField()
    price = db.FloatField(default=0)
    pub_date = db.DateTimeField(default=datetime.datetime.now)
    
@app.route("/api")
def index(title,description,price,pub_date):
    Movie.objects().delete()
    Movie(title,description,price,pub_date).save()
    todos = Movie.objects().to_json()
    return Response(todos, mimetype="application/json", status=200)

@app.route("/feed_rss")
def feed_rss():
    fg = FeedGenerator()
    fg.title('https://example.com/api/')
    fg.description('Some Testfeed')
    fg.price,( {'price':'20.0'} )
    fg.pub_date('01-20-10')
    

    atomfeed = fg.atom_str(pretty=True) # Get the ATOM feed as string
    rssfeed  = fg.rss_str(pretty=True) # Get the RSS feed as string

  
if __name__ == "__main__":
    app.run(debug=True, port=5000)
