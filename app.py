# import necessary libraries
from flask import Flask, render_template
import pymongo
import scrapeMars 

# create an instance of flask app
app = Flask(__name__)

client = pymongo.MongoClient()
db = client.astronomy_db
collection = db.mars_scrape

@app.route("/scrape")
def scrape():

    db.collection.delete_many({})
    data = scrapeMars.scrape()
    db.collection.insert_one(data)
    return 'Completed Scrapping the Data!'

# create route that renders the html template
@app.route("/")
def home():
    data = db.collection.find_one()
    return render_template('index.html',data=data)

# run as a python script
if __name__ == "__main__":
    app.run(debug=True)