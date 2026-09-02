from os import getenv
from flask import Flask
from dotenv import load_dotenv

# Register ENV variables
load_dotenv()

from models.db import db
from routes import register_routes
from config import Config

app = Flask(__name__)


# Register routes
register_routes(app)

# Register config
config_class = Config()
app.config.from_object(config_class)


# Register database
db.init_app(app)


with app.app_context():
    if getenv("CREATE_TABLES_ON") == True:
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
