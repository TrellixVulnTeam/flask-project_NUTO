from flask_migrate import Migrate
from src.ext.db import models #


migrate = Migrate()

def init_app(app):
  migrate.init_app(app)
