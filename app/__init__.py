"""
The actual web application.
"""

### IMPORTS

import logging
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

### CONSTANTS & DEFINES

__version__ = "0.5"


### CODE ###

# logging configuration
logging.basicConfig (format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel (logging.DEBUG)

# application configuration
app = Flask(__name__)
app.config.from_object ('config')
db = SQLA (app)

appbuilder = AppBuilder (app, db.session)

migrate = Migrate (app, db)
manager = Manager (app)
manager.add_command('db', MigrateCommand)

# build the models and views
from app import models, views, admin, utils


### END ###
