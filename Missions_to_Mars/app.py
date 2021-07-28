from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of dat from the mongo database
    mars_dict = mongo.db.mars_dict.find_one()

    # Return template and data
    return render_template("index.html", surface=mars_dict)


@app.route("/scrape")
def scrape():
    
    # Run the scrape function
    mars_dict = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.surface.update({}, surface_data, upsert=True)
    
    return redirect("/")
    #return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

