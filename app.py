import os
from dotenv import load_dotenv
if os.path.exists("./.env"):
    load_dotenv()
from flask import Flask
from dotenv import load_dotenv
from requests.packages import urllib3
from flask_cors import CORS
import os

from api.search_module import search_blueprint
from api.json_encoder import MyEncoder


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
app.register_blueprint(search_blueprint, name="search_api")
app.json_encoder = MyEncoder


if (not os.getenv('PRODUCTION')):
    print('RUNNING IN DEVELOPMENT ENV...')
    cors = CORS(app, supports_credentials=True)

@app.route("/")
def root():
    return "<h1>check if someone is PEP or in a sanction lists</h1>"


if __name__ == '__main__':
    app.run()