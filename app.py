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
astrology_collection = db['astrology']

#Custom functions
def calculate_age(birth_date):
    today = datetime.now()
    birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def find_astrological_sign(birthdate_str):
    # Convert birthdate to datetime object
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
    
    # Calculate the day of the year
    day_of_year = birthdate.timetuple().tm_yday
    print(f'Birth day of year {day_of_year}')
    
    # Find the record based on day_of_year
    result = astrology_collection.find_one({
        "dates.from.day_of_year": {"$lte": day_of_year},
        "dates.to.day_of_year": {"$gte": day_of_year}
    })

    #print(result)
    
    if result:
        return result
    else:
        return None
    
def convert_birthdate_to_countdown_format(birthdate_str):
    # Convert dd/mm/yyyy to datetime object
    birthdate = datetime.strptime(birthdate_str, '%d/%m/%Y')
    
    # Replace year with current year
    current_year = datetime.now().year
    birthdate = birthdate.replace(year=current_year)
    
    # Convert to desired format
    formatted_date = birthdate.strftime('%b %d, %Y 00:00:00')
    return formatted_date

@app.route('/')
def countdown():
    bdate = config['birthdate']
    #print(bdate)
    age = calculate_age(bdate)
    #print(age)
    name = config['name']
    #print(name)
    sign = find_astrological_sign(bdate)
    #print(sign)
    bmessage = config['bday_message']
    #print(bmessage)
    bgif_url = config['gif_url']
    #print(bgif_url)
    # Convert birthdate to the required format
    birthdate_formatted = convert_birthdate_to_countdown_format(bdate)
    #print(birthdate_formatted)
    sender_name = config['sender_name']
    #print(sender_name)
    # Existing countdown route logic
    return render_template('countdown.html', name= name,age=age,astronomy=sign, birthdate=bdate, message=bmessage, gif_url=bgif_url,bdate_formatted=birthdate_formatted,sender_name=sender_name)

@app.route('/travel')
def travel_recommendation():
    # Existing travel recommendation logic
    places = list(wishlist_places_collection.find({}, {'_id': 0}))  # Exclude '_id' field
    print(f'List of wishlist place : {places}')
    return render_template('travel_recommendation.html', destinations=places)

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
        traveled = wishlist_places_collection.find({"isTraveled": True})
        untraveled = wishlist_places_collection.find({"isTraveled": False})
        response = {"traveled": traveled, "untraveled": untraveled}
        #print('Places fetched:', response)  # Debug statement
        return jsonify(response)
    except Exception as e:
        print('Error:', e)  # Debug statement
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_place_details/<place_id>')
def get_place_details(place_id):
    place = wishlist_places_collection.find_one({"_id": place_id})
    if place:
        return jsonify({
            'name': place.get('name'),
            'lat': place.get('lat'),
            'long': place.get('long'),
            'date': place.get('date'),
            'photo': place.get('photo'),
            'google_sheet_url': place.get('google_sheet_url'),
            'travelled': place.get('travelled')
        })
    else:
        return jsonify({}), 404

@app.route('/food_recommendation', methods=['GET', 'POST'])
def food_recommendation():
    search_results = []

    if request.method == 'POST':
        selected_cuisines = request.form.get('cuisine')
        #print(selected_cuisines)
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
    HOST = '0.0.0.0'
    PORT = 80
    app.run(host=HOST, port=PORT, debug=True)
