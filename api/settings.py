import os

# API parameters
# /search endpoint
API_SEARCH_QUERY = "q"
API_FULL_RESULTS = "full"

# neskor mozno doplnit o databazu a veci, podla toho z kadial budeme tahat data
MONGO_SERVER_URL = str(os.getenv('MONGO_SERVER_URL') or 'localhost')
MONGO_SERVER_PORT = str(os.getenv('MONGO_SERVER_PORT') or 27017)
MONGO_USER = str(os.getenv('MONGO_USER') or 'fiitkar')
MONGO_PASSWORD = str(os.getenv('MONGO_PASSWORD') or 'fiitkar')
MONGO_DB = str(os.getenv('MONGO_DB') or 'adversea-pep')
MONGO_PEP_COLLECTION = str(os.getenv('MONGO_PEP_COLLECTION') or 'pep')
MONGO_SANCTIONS_COLLECTION = str(os.getenv('MONGO_SANCTIONS_COLLECTION') or 'sanctions')