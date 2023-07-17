from flask import Blueprint
from flask.json import jsonify
from flask import request
import re

import api.settings as settings
import api.queries as queries
from .db_connector import Database

# /peps/search/
search_blueprint = Blueprint("search_routes", __name__, url_prefix="/peps/")


# look for person in our pep database
def find_pep_in_db(query):
    # first we look in caption field
    pep = Database.find_one(settings.MONGO_PEP_COLLECTION, 
                {'caption': re.compile(query, re.IGNORECASE)},              # case insensitive search
                {"caption":1, "properties":1, "schema":1, "_id": False})    # fields to select

    # if unsuccessful then we try looking using combination of first name and last name fields
    if pep is None:
        queries.FIND_BY_FIRSTNAME_AND_LASTNAME['$expr']['$regexMatch']['regex'] = query
        pep = Database.find_one(settings.MONGO_PEP_COLLECTION, 
                    queries.FIND_BY_FIRSTNAME_AND_LASTNAME,
                    {"caption":1, "properties":1, "schema":1, "_id": False})        
    return pep


# look for results in our pep and sanction database
def find_by_name(query, collection):
    # first we look in caption field
    results = Database.find_one(collection, 
                {'name': re.compile(query, re.IGNORECASE)},                                     # case insensitive search
                {"first_seen":False, "last_seen":False, "last_change":False, "_id": False})    # fields to ignore
    
    return results


# select only useful info from the found results
def select_useful_data(document):
    return document


# TODO: dorobit neskor !!!!!!!!!!!!!!!!!!!!!!!!
# look for person via pepchecker
# def find_by_pepchecker(query):
#     default_headers = make_headers()
#     http = ProxyManager('http://tor-1:8888', proxy_headers=default_headers)
#     apiKey = 'test-00000000-0000-0000-0000-000000000000'

#     name_parts = query.split()
#     firstName = name_parts[0]
#     lastName = ' '.join(name_parts[1:])

#     response = http.request('GET', 'https://pepchecker.com/api/v1/check?firstName=' + firstName + '&lastName=' + lastName, 
#                             headers={'api-key': apiKey})
#     response_data = json.loads(response.data)
#     if response_data[0]['field'] == None:
#         return None
#     else:
#         response_data = response_data['pepList'][0]
    
#     # compare names to check if we found the correct person
#     # pepchecker can return similar names if ours is not found 
#     if response_data['firstName'] + response_data['lastName'] != query:
#         return None
#     else:
#         return response_data


# main function for searching
@search_blueprint.route("/search", methods=["GET"])
def search():
    query = request.args.get(settings.API_SEARCH_QUERY, default=None, type=str)
    full_results = request.args.get(settings.API_FULL_RESULTS, default=True, type=bool)

    if query is None:
        return "Invalid input, please provide 'q' parameter", 400

    Database.initialize()

    # first, we try to look for person in our pep and sanctions database
    pep = find_by_name(query, settings.MONGO_PEP_COLLECTION)
    sanctions = find_by_name(query, settings.MONGO_SANCTIONS_COLLECTION)

    # if not found in db, we can try using pepchecker
    # if pep is None:
    #     pep = find_by_pepchecker(query)

    response = {
        "query": query,
        "pep": pep,
        "sanctions": sanctions
    }
    
    return jsonify(response)
