from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#from scrape_mars import scrape_info
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of dat from the mongo database
    surface_data = mongo.db.surface.find_one()

    # Return template and data
    return render_template("index.html", surface=surface_data)


@app.route("/scrape")
def scrape():
    
    # Run the scrape function
    surface_data = scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.surface.update({}, surface_data, upsert=True)
    
    return redirect("/")
    #return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

