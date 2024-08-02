import requests
from flask import Flask, jsonify, redirect, render_template, request, url_for
import json
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

def load_config():
    with open('secret.json') as f:
        return json.load(f)

config = load_config()

# Example API key (replace with your own)
YOUTUBE_API_KEY = config['youtube_api_key']

# MongoDB client setup
client = MongoClient(config['mongodb_uri'])
db = client.travel_recommendations
traveled_places_collection = db.traveled_places

@app.route('/')
def countdown():
    # Existing countdown route logic
    return render_template('countdown.html', name= "Rim")

@app.route('/travel')
def travel_recommendation():
    # Existing travel recommendation logic
    return render_template('travel_recommendation.html')

@app.route('/mark_traveled', methods=['POST'])
def mark_traveled():
    place_name = request.form['place_name']
    date_traveled = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    traveled_places_collection.insert_one({
        'place_name': place_name,
        'date_traveled': date_traveled
    })
    
    return redirect(url_for('travel_recommendation'))

@app.route('/traveled_places', methods=['GET'])
def traveled_places():
    traveled_places = list(traveled_places_collection.find({}, {'_id': 0}))
    return jsonify(traveled_places)

@app.route('/food_recommendation', methods=['GET', 'POST'])
def food_recommendation():
    search_results = []

    if request.method == 'POST':
        selected_cuisines = request.form.get('cuisine')
        search_query = f'Best recommended {selected_cuisines} cuisine'

        # Fetch videos based on search query
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'part': 'snippet',
            'q': search_query,
            'type': 'video',
            'key': YOUTUBE_API_KEY,
            'maxResults': 10
        }
        response = requests.get(search_url, params=params)
        search_results = response.json().get('items', [])

    return render_template('food_recommendation.html', search_results=search_results)

@app.route('/songs', methods=['GET', 'POST'])
def song_recommendation():
    search_query = "todays trending solo indie song" # request.args.get('search', '')  # Get search query from URL
    if search_query:
        # Fetch videos based on search query
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'part': 'snippet',
            'q': search_query,
            'type': 'video',
            'key': YOUTUBE_API_KEY,
            'maxResults': 10
        }
        response = requests.get(search_url, params=params)
        search_results = response.json().get('items', [])
    else:
        search_results = []

    return render_template('song_recommendation.html', search_results=search_results)

if __name__ == '__main__':
    app.run(debug=True)
