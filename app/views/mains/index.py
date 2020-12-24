from . import main
from flask import render_template
from flask_login import current_user
from ... import logger


@main.route('/')
def index():
    """登入頁"""
    # return "Hello {id}".format(id=current_user.is_authenticated)

    return render_template('mains/index.html', title="首頁")
