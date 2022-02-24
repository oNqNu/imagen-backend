import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('processing', __name__, url_prefix='/processing')

@bp.route('/hello')
def hello():
    return 'Hello, oNqNu!'