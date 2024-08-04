from pymongo import MongoClient
import json

def load_config():
    with open('secret.json') as f:
        return json.load(f)

config = load_config()

# Function to connect to MongoDB
def connect_to_mongodb():
    # MongoDB connection
    client = MongoClient(config['mongodb_uri'])
    db = client['Alfred']
    wishlist_places_collection = db['wishlist_places']
    return wishlist_places_collection


# Function to add a place to the wishlist
def add_place_to_wishlist(collection):
    print("Enter the details for the new place:")
    name = input("Name: ")
    lat = input("Latitude: ")
    long = input("Longitude: ")
    date = input("Date: ")
    photo = input("Photo URL: ")
    google_sheet_url = input("Google Sheet URL for Itinerary: ")

    place = {
        'name': name,
        'lat': lat,
        'long': long,
        'date': date,
        'photo': photo,
        'google_sheet_url': google_sheet_url
    }

    # Insert the place into the collection
    collection.insert_one(place)
    print("Place added successfully!")

# Main function
def main():
    collection = connect_to_mongodb()
    while True:
        add_place_to_wishlist(collection)
        cont = input("Do you want to add another place? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == '__main__':
    main()