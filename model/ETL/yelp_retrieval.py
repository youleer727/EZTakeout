import argparse
import json
import pprint
import requests
import sys
import urllib
import csv
from urllib2 import HTTPError
from urllib import quote
from urllib import urlencode


CLIENT_ID = ''
CLIENT_SECRET = ''

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'


# Defaults for our simple example.
#DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'New York, NY'
SEARCH_LIMIT = 50
TOTAL_COUNT = 0

def read_credentials():
    global CLIENT_ID, CLIENT_SECRET
    with open('yelp_secret.txt', 'rb') as f:
        client = f.readlines()
    CLIENT_ID = client[0].strip()
    CLIENT_SECRET = client[1].strip()


def obtain_bearer_token(host, path):
    """Given a bearer token, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        str: OAuth bearer token, obtained using client_id and client_secret.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    assert CLIENT_ID, "Please supply your client_id."
    assert CLIENT_SECRET, "Please supply your client_secret."
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token


def request(host, path, bearer_token, url_params=None):
    """Given a bearer token, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        bearer_token (str): OAuth bearer token, obtained using client_id and client_secret.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }

    # print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(bearer_token, location):
    """Query the Search API by a search term and location.
    Args:
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'offset': 50*TOTAL_COUNT
    }
    return request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params)


def get_business(bearer_token, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, bearer_token)


def query_api(location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)
    response = search(bearer_token, location)
    businesses = response.get('businesses')
    if not businesses:
        raise KeyError
    with open('ny_data.csv', 'a') as f:
        fieldnames = ['id', 'name', 'price', 'rating', 'phone', 'latitude', 'longitude']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
        for index, b in enumerate(businesses):
            temp = {}
            print b
            if 'price' in b.keys():
                temp['price'] = b['price'].encode('utf-8')
            if 'name' in b.keys():
                temp['name'] = b['name'].encode('utf-8')
            if 'id' in b.keys():
                temp['id'] = b['id'].encode('utf-8')
            if 'rating' in b.keys():
                temp['rating'] = str(b['rating']).encode('utf-8')
            if 'display_phone' in b.keys():
                temp['phone'] = b['display_phone'].encode('utf-8')
            if 'coordinates' in b.keys():
                if ('latitude' in b['coordinates'].keys()) and ('longitude' in b['coordinates'].keys()):
                    temp['latitude'] = str(b['coordinates']['latitude']).encode('utf-8')
                    temp['longitude'] = str(b['coordinates']['longitude']).encode('utf-8')
            if len(temp.keys())==len(fieldnames):
                writer.writerow(temp)


def main():
    global TOTAL_COUNT
    read_credentials()
    fieldnames = ['id', 'name', 'price', 'rating', 'phone', 'latitude', 'longitude']
    with open('ny_data.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
    try:
        while TOTAL_COUNT < 2818:
            print(TOTAL_COUNT)
            try:
                query_api('New York, NY')
            except HTTPError:
                continue
            except KeyError:
                continue
            else:
                TOTAL_COUNT += 1
    except:
        pass


if __name__ == '__main__':
    main()
