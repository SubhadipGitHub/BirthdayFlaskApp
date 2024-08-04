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
    astrology_collection = db['astrology']
    return astrology_collection

# JSON data
data = [
    {
      "name": "Aries",
      "dates": {
        "from": {
          "dd_mm": "21/03",
          "day_of_year": 80
        },
        "to": {
          "dd_mm": "19/04",
          "day_of_year": 109
        }
      },
      "traits": [
        {
          "trait": "Energetic",
          "description": "Aries individuals are full of energy and enthusiasm. They approach life with a vibrant and dynamic attitude.",
          "image_url": "https://example.com/energetic.jpg"
        },
        {
          "trait": "Courageous",
          "description": "Aries are known for their bravery and willingness to take risks. They face challenges head-on with confidence.",
          "image_url": "https://example.com/courageous.jpg"
        },
        {
          "trait": "Impulsive",
          "description": "Aries can act on a whim, often without thinking through the consequences. Their spontaneous nature can lead to adventurous experiences.",
          "image_url": "https://example.com/impulsive.jpg"
        },
        {
          "trait": "Optimistic",
          "description": "Aries have a positive outlook on life. They believe in the best possible outcome and maintain a hopeful attitude.",
          "image_url": "https://example.com/optimistic.jpg"
        }
      ]
    },
    {
      "name": "Taurus",
      "dates": {
        "from": {
          "dd_mm": "20/04",
          "day_of_year": 110
        },
        "to": {
          "dd_mm": "20/05",
          "day_of_year": 140
        }
      },
      "traits": [
        {
          "trait": "Reliable",
          "description": "Taurus individuals are dependable and trustworthy. Others can count on them to follow through on commitments.",
          "image_url": "https://example.com/reliable.jpg"
        },
        {
          "trait": "Patient",
          "description": "Taurus people exhibit great patience and persistence. They are willing to wait for the right moment to act.",
          "image_url": "https://example.com/patient.jpg"
        },
        {
          "trait": "Practical",
          "description": "Taurus is known for their practical approach to life. They prefer realistic and feasible solutions over abstract ideas.",
          "image_url": "https://example.com/practical.jpg"
        },
        {
          "trait": "Stubborn",
          "description": "Taurus can be quite set in their ways. Their determination can sometimes come across as obstinacy.",
          "image_url": "https://example.com/stubborn.jpg"
        }
      ]
    },
    {
      "name": "Gemini",
      "dates": {
        "from": {
          "dd_mm": "21/05",
          "day_of_year": 141
        },
        "to": {
          "dd_mm": "20/06",
          "day_of_year": 171
        }
      },
      "traits": [
        {
          "trait": "Adaptable",
          "description": "Geminis are highly flexible and can adjust to new situations with ease. They thrive in changing environments.",
          "image_url": "https://example.com/adaptable.jpg"
        },
        {
          "trait": "Outgoing",
          "description": "Geminis are social butterflies who enjoy engaging with others. They have a natural charm and are often the life of the party.",
          "image_url": "https://example.com/outgoing.jpg"
        },
        {
          "trait": "Intelligent",
          "description": "Geminis possess sharp minds and a quick wit. They are curious and enjoy learning about a variety of topics.",
          "image_url": "https://example.com/intelligent.jpg"
        },
        {
          "trait": "Indecisive",
          "description": "Geminis can struggle with making decisions. Their dual nature often leads them to weigh multiple options before choosing.",
          "image_url": "https://example.com/indecisive.jpg"
        }
      ]
    },
    {
      "name": "Cancer",
      "dates": {
        "from": {
          "dd_mm": "21/06",
          "day_of_year": 172
        },
        "to": {
          "dd_mm": "22/07",
          "day_of_year": 203
        }
      },
      "traits": [
        {
          "trait": "Tenacious",
          "description": "Cancers are known for their determination and perseverance. They hold on to their goals and work diligently to achieve them.",
          "image_url": "https://example.com/tenacious.jpg"
        },
        {
          "trait": "Highly Imaginative",
          "description": "Cancers have vivid imaginations and a creative mind. They often come up with unique and innovative ideas.",
          "image_url": "https://example.com/imaginative.jpg"
        },
        {
          "trait": "Loyal",
          "description": "Cancers are fiercely loyal to their loved ones. They value trust and commitment in their relationships.",
          "image_url": "https://example.com/loyal.jpg"
        },
        {
          "trait": "Emotional",
          "description": "Cancers experience emotions deeply and are very empathetic. They are in tune with their own feelings and those of others.",
          "image_url": "https://example.com/emotional.jpg"
        }
      ]
    },
    {
      "name": "Leo",
      "dates": {
        "from": {
          "dd_mm": "23/07",
          "day_of_year": 204
        },
        "to": {
          "dd_mm": "22/08",
          "day_of_year": 235
        }
      },
      "traits": [
        {
          "trait": "Creative",
          "description": "Leos are bursting with creativity and artistic talent. They have a flair for drama and self-expression.",
          "image_url": "https://example.com/creative.jpg"
        },
        {
          "trait": "Generous",
          "description": "Leos are known for their generosity and big-hearted nature. They love to give and share with others.",
          "image_url": "https://example.com/generous.jpg"
        },
        {
          "trait": "Warm-hearted",
          "description": "Leos have a warm and caring nature. They are affectionate and often go out of their way to make others feel loved.",
          "image_url": "https://example.com/warm-hearted.jpg"
        },
        {
          "trait": "Cheerful",
          "description": "Leos are naturally upbeat and cheerful. Their positive energy can lift the spirits of those around them.",
          "image_url": "https://example.com/cheerful.jpg"
        }
      ]
    },
    {
      "name": "Virgo",
      "dates": {
        "from": {
          "dd_mm": "23/08",
          "day_of_year": 236
        },
        "to": {
          "dd_mm": "22/09",
          "day_of_year": 265
        }
      },
      "traits": [
        {
          "trait": "Loyal",
          "description": "Virgos are steadfastly loyal to those they care about. They build strong and lasting relationships based on trust.",
          "image_url": "https://example.com/loyal.jpg"
        },
        {
          "trait": "Analytical",
          "description": "Virgos have a keen eye for detail and a methodical approach. They excel at problem-solving and critical thinking.",
          "image_url": "https://example.com/analytical.jpg"
        },
        {
          "trait": "Kind",
          "description": "Virgos are kind-hearted and compassionate. They are always ready to help others and show empathy.",
          "image_url": "https://example.com/kind.jpg"
        },
        {
          "trait": "Practical",
          "description": "Virgos have a practical mindset and prefer logical solutions. They are grounded and realistic in their approach.",
          "image_url": "https://example.com/practical.jpg"
        }
      ]
    },
    {
      "name": "Libra",
      "dates": {
        "from": {
          "dd_mm": "23/09",
          "day_of_year": 266
        },
        "to": {
          "dd_mm": "22/10",
          "day_of_year": 295
        }
      },
      "traits": [
        {
          "trait": "Cooperative",
          "description": "Libras excel at working with others and fostering teamwork. They value harmony and collaboration.",
          "image_url": "https://example.com/cooperative.jpg"
        },
        {
          "trait": "Diplomatic",
          "description": "Libras are skilled at navigating social situations with tact. They are great mediators and peacekeepers.",
          "image_url": "https://example.com/diplomatic.jpg"
        },
        {
          "trait": "Gracious",
          "description": "Libras are polite and well-mannered. They approach interactions with kindness and respect.",
          "image_url": "https://example.com/gracious.jpg"
        },
        {
          "trait": "Fair-minded",
          "description": "Libras have a strong sense of justice and fairness. They strive to make balanced and unbiased decisions.",
          "image_url": "https://example.com/fair-minded.jpg"
        }
      ]
    },
    {
      "name": "Scorpio",
      "dates": {
        "from": {
          "dd_mm": "23/10",
          "day_of_year": 296
        },
        "to": {
          "dd_mm": "21/11",
          "day_of_year": 325
        }
      },
      "traits": [
        {
          "trait": "Resourceful",
          "description": "Scorpios are adept at finding solutions to problems. They are resilient and can make the most out of any situation.",
          "image_url": "https://example.com/resourceful.jpg"
        },
        {
          "trait": "Brave",
          "description": "Scorpios exhibit great courage and fearlessness. They face challenges head-on and are not easily intimidated.",
          "image_url": "https://example.com/brave.jpg"
        },
        {
          "trait": "Passionate",
          "description": "Scorpios feel things intensely and are deeply passionate. They are driven by their emotions and desires.",
          "image_url": "https://example.com/passionate.jpg"
        },
        {
          "trait": "Stubborn",
          "description": "Scorpios can be very determined and persistent. Once they set their mind on something, they pursue it relentlessly.",
          "image_url": "https://example.com/stubborn.jpg"
        }
      ]
    },
    {
      "name": "Sagittarius",
      "dates": {
        "from": {
          "dd_mm": "22/11",
          "day_of_year": 326
        },
        "to": {
          "dd_mm": "21/12",
          "day_of_year": 355
        }
      },
      "traits": [
        {
          "trait": "Generous",
          "description": "Sagittarians are known for their generosity and open-heartedness. They love to share their time and resources with others.",
          "image_url": "https://example.com/generous.jpg"
        },
        {
          "trait": "Idealistic",
          "description": "Sagittarians have high ideals and a strong sense of purpose. They are driven by their beliefs and aspirations.",
          "image_url": "https://example.com/idealistic.jpg"
        },
        {
          "trait": "Great Sense of Humor",
          "description": "Sagittarians have a great sense of humor and love to make others laugh. Their wit and charm are infectious.",
          "image_url": "https://example.com/humor.jpg"
        },
        {
          "trait": "Impatient",
          "description": "Sagittarians can be quite impatient. They dislike waiting and prefer to act quickly to achieve their goals.",
          "image_url": "https://example.com/impatient.jpg"
        }
      ]
    },
    {
      "name": "Capricorn",
      "dates": {
        "from": {
          "dd_mm": "22/12",
          "day_of_year": 356
        },
        "to": {
          "dd_mm": "19/01",
          "day_of_year": 19
        }
      },
      "traits": [
        {
          "trait": "Responsible",
          "description": "Capricorns are highly responsible and dependable. They take their duties seriously and can be relied upon.",
          "image_url": "https://example.com/responsible.jpg"
        },
        {
          "trait": "Disciplined",
          "description": "Capricorns exhibit great self-discipline and control. They are focused and work diligently towards their goals.",
          "image_url": "https://example.com/disciplined.jpg"
        },
        {
          "trait": "Self-Controlled",
          "description": "Capricorns have excellent self-control. They are able to regulate their emotions and actions effectively.",
          "image_url": "https://example.com/self-controlled.jpg"
        },
        {
          "trait": "Good Managers",
          "description": "Capricorns have strong managerial skills. They are organized and excel at leading and coordinating efforts.",
          "image_url": "https://example.com/managers.jpg"
        }
      ]
    },
    {
      "name": "Aquarius",
      "dates": {
        "from": {
          "dd_mm": "20/01",
          "day_of_year": 20
        },
        "to": {
          "dd_mm": "18/02",
          "day_of_year": 49
        }
      },
      "traits": [
        {
          "trait": "Progressive",
          "description": "Aquarians are forward-thinking and progressive. They embrace new ideas and innovation.",
          "image_url": "https://example.com/progressive.jpg"
        },
        {
          "trait": "Original",
          "description": "Aquarians have a unique and original perspective. They think outside the box and are often ahead of their time.",
          "image_url": "https://example.com/original.jpg"
        },
        {
          "trait": "Independent",
          "description": "Aquarians value their independence highly. They prefer to act on their own terms and resist conformity.",
          "image_url": "https://example.com/independent.jpg"
        },
        {
          "trait": "Humanitarian",
          "description": "Aquarians have a strong humanitarian streak. They care deeply about social issues and work towards the betterment of society.",
          "image_url": "https://example.com/humanitarian.jpg"
        }
      ]
    },
    {
      "name": "Pisces",
      "dates": {
        "from": {
          "dd_mm": "19/02",
          "day_of_year": 50
        },
        "to": {
          "dd_mm": "20/03",
          "day_of_year": 79
        }
      },
      "traits": [
        {
          "trait": "Compassionate",
          "description": "Pisces are deeply compassionate and empathetic. They feel others' emotions as if they were their own.",
          "image_url": "https://example.com/compassionate.jpg"
        },
        {
          "trait": "Artistic",
          "description": "Pisces have a natural affinity for the arts. They express themselves creatively and appreciate beauty in all forms.",
          "image_url": "https://example.com/artistic.jpg"
        },
        {
          "trait": "Intuitive",
          "description": "Pisces possess strong intuition and psychic abilities. They trust their instincts and often rely on their gut feelings.",
          "image_url": "https://example.com/intuitive.jpg"
        },
        {
          "trait": "Gentle",
          "description": "Pisces are gentle and kind-hearted. They approach life with a soft touch and are sensitive to others' needs.",
          "image_url": "https://example.com/gentle.jpg"
        }
      ]
    }
  ]

# Insert the data into the collection
# Function to add a place to the wishlist
def bulk_load_astrologic_sign(collection):
    collection.insert_many(data)

# Main function
def main():
    astrology_collection = connect_to_mongodb()
    while True:
        try:
            bulk_load_astrologic_sign(astrology_collection)
            print("Data inserted successfully")
            break
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    main()