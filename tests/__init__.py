from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)
# ... existing app configurations ...

talisman = Talisman(app)
CORS(app)  # This line enables CORS for all routes
