
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