from functools import wraps
from flask import session, redirect, url_for

def trainer_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('trainer'):
            return redirect(url_for('auth.index'))
        return f(*args, **kwargs)
    return decorated_function