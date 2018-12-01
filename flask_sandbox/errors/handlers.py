from flask import Blueprint, render_template

from flask_sandbox.config import error_p

errors = Blueprint('errors',__name__)

@errors.app_errorhandler(404)
def error_404(error):

    return render_template('errors/404.html',param=error_p, error=error), 404

@errors.app_errorhandler(403)
def error_403(error):
    print(dir(error))
    return render_template('errors/403.html',param=error_p, error=error), 403

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html',param=error_p, error=error), 500
