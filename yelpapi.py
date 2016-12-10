from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
    auth = Oauth1Authenticator(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        token=os.environ['TOKEN'],
        token_secret=os.environ['TOKEN_SECRET']
    )

    client = Client(auth)

    params = {
        'term': term,
        'lang': 'en',
        'limit': 10,
        'sort': 2
    }

    response = client.search(location, **params)

    # creates an empty list
    businesses = []

    for business in response.businesses:
        # turn empty list into a dictionary
        businesses.append({"name": business.name, 
        	"rating": business.rating_img_url, 
        	"photo": business.image_url,
            "url": business.url 
        })

    return businesses

businesses = get_businesses('Daytona Beach', 'food')

#print(businesses)