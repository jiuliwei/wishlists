from enum import Enum
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger("flask.app")
db = SQLAlchemy()

class DataValidationError(ValueError):
    pass

class EntityNotFoundError(KeyError):
  pass

class Availability(Enum):
  Available = 1
  Unavailable = 0