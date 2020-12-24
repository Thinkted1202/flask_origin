import re, socket
from flask import current_app, url_for
from lxml.html.clean import Cleaner


def overwrite_url_for(endpoint, **values):
    """針對static設定的版本號 清除Browser的cache"""
    if endpoint == 'static':
        values['ts'] = current_app.config['STATIC_VERSION']
    return url_for(endpoint, **values)


def clear_html(in_str: str, tag_whitelist: list = []):
    """清除html或js"""
    if not in_str:
        return in_str

    cleaner = Cleaner(allow_tags=tag_whitelist, remove_unknown_tags=False)
    if not tag_whitelist:
        cleaner.html = True
    cleaner.javascript = True
    cleaner.html = True
    out_str = cleaner.clean_html(in_str)

    return re.sub(r'</p>$', '', re.sub(r'^<p>', '', out_str))


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
