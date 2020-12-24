from flask import Blueprint, session
from app.helpers.utils_helper import overwrite_url_for

main = Blueprint('main', __name__)
from . import index, errors


@main.before_request
def permission_hook():
    """統一對每一頁做權限控管"""
    pass


@main.app_context_processor
def logined_init_processor():
    """登入後才執行"""
    return dict()


@main.app_context_processor
def init_processor():
    """借助app_context_processor我們可以讓所有自定義變量在模板中可見"""
    header = {
        'title': "Eagleeye"
    }
    return dict(header=header, url_for=overwrite_url_for)
