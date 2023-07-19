## How to run
  * git clone <url>
  * go to repository folder
  * python -m venv .\venv
  * .\venv\Scripts\activate
  * pip install -r requirements.txt
  * python app.py

## Search in PEP and sanctions database

Parameters:

* q - search query (usually name, search is case and accent insensitive)
* full - returns full or narrowed results (not yet implemented, default value is true)

Examples:
```
curl -X GET http://localhost:5000/peps/search?q=marian+kocner
```
