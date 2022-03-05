from flask import Flask

from src.ext import admin, auth, cli, config, db, hooks, migrate, site, toolbar, login


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    
    # db.init_app(app)
    # migrate.init_app(app)
    # auth.init_app(app)
    # admin.init_app(app)
    # cli.init_app(app)
    # toolbar.init_app(app)
    # site.init_app(app)
    # hooks.init_app(app)

    return app
