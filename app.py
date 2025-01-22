from flask import Flask, render_template, jsonify
import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
app = Flask(__name__)
app.secret_key = os.environ['FLASK_KEY']


# MongoDB Connection
uri = os.environ['MONGODB_URI']
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['portfolio'] 

@app.route('/')
def index():
    projects = list(db.projects.find())  # Fetch only the first 4 projects
    total_projects = db.projects.count_documents({})
    has_more_projects = len(projects) < total_projects  # Check if there are more projects
    publications = list(db.publications.find())  # Fetch all publications

    return render_template('index.html', 
                           projects=projects, 
                           publications=publications, 
                           has_more_projects=has_more_projects)

if __name__ == '__main__':
    app.run(debug=True)