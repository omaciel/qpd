# coding: utf-8
"""This module exists to avoid circular imports when importing db object"""
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()
