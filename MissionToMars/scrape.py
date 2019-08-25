# import necessary libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo
import MissionToMars

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/marsmission_app")
# Create an instance of Flask
app = Flask(__name__)

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)



@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_mission_dict = MissionToMars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_mission_dict, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
