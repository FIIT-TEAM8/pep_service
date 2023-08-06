
# query for searching in first name and last name fields
# used only when caption field has fucky formating
FIND_BY_FIRSTNAME_AND_LASTNAME = {
    "$expr": {
        "$regexMatch": {
            "input": {"$concat": [{"$arrayElemAt": ["$properties.firstName", 0]}, " ", {"$arrayElemAt": ["$properties.lastName", 0]}]},
            "regex": '$query',
            "options": "i"
        }
    }
}


# query for searching in the alias field
# used only when name_ascii finds nothing
FIND_BY_ALIAS = {
    "aliases": {
        "$regex": '$query',
        "$options": "i"
  }
}


FIELDS_TO_IGNORE = {"first_seen":False, "last_seen":False, "last_change":False, "_id": False}