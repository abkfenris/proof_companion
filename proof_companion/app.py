from eve import Eve
from eve_sqlalchemy import SQL as _SQL
from eve_sqlalchemy.validation import ValidatorSQL

from config import config

from .core import db
from .models import Contact


class SQL(_SQL):
    driver = db


def create_app(config_name):
    app = Eve(validator=ValidatorSQL, data=SQL, settings=config[config_name].EVE_SETTINGS)
    app.config.from_object(config[config_name])

    db.init_app(app)

    return app
