#!/usr/bin/env python3
""" Initialization Module"""

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
