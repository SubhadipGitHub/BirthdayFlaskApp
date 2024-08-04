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

# MongoDB connection
client = MongoClient(config['mongodb_uri'])
db = client['Alfred']
wishlist_places_collection = db['wishlist_places']

@app.route('/')
def countdown():
    # Existing countdown route logic
    return render_template('countdown.html', name= "Rim")

@app.route('/travel')
def travel_recommendation():
    # Existing travel recommendation logic
    return render_template('travel_recommendation.html')

@app.route('/save_place', methods=['POST'])
def save_place():
    try:
        data = request.json
        data['date'] = datetime.now()
        print('Data received for saving:', data)  # Debug statement
        wishlist_places_collection.update_one(
            {"name": data['name'], "lat": data['lat'], "lng": data['lng']},
            {"$set": data},
            upsert=True
        )
        response = {"status": "success", "data": data}
        print('Response:', response)  # Debug statement
        return jsonify(response)
    except Exception as e:
        print('Error:', e)  # Debug statement
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_places', methods=['GET'])
def get_places():
    try:
        traveled = list(wishlist_places_collection.find({"isTraveled": True}))
        untraveled = list(wishlist_places_collection.find({"isTraveled": False}))
        response = {"traveled": traveled, "untraveled": untraveled}
        print('Places fetched:', response)  # Debug statement
        return jsonify(response)
    except Exception as e:
        print('Error:', e)  # Debug statement
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/food_recommendation', methods=['GET', 'POST'])
def food_recommendation():
    search_results = []

    if request.method == 'POST':
        selected_cuisines = request.form.get('cuisine')
        print(selected_cuisines)
        search_query = f'Unique {selected_cuisines} cuisine recipes'

        # Fetch videos based on search query
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        params = {
            'part': 'snippet',
            'q': search_query,
            'type': 'video',
            'key': YOUTUBE_API_KEY,
            'maxResults': 10,
            'order': 'viewCount',  # Order by view count to find popular videos
            'regionCode': 'US'    # Adjust region if needed
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
