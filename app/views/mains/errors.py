from flask import render_template, request, jsonify
from . import main

# template_folder
tpl_folder = 'mains/errors/'


@main.app_errorhandler(403)
def forbidden(e):
    """403 錯誤處理"""
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'forbidden'})
        response.status_code = 403
        return response
    return render_template(tpl_folder + '403.html', description=e.description), 403


@main.app_errorhandler(404)
def page_not_found(e):
    """ 404 錯誤處理 """
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template(tpl_folder + '404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    """ 500 錯誤處理 """
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'internal server error'})
        response.status_code = 500
        return response
    return render_template(tpl_folder + '500.html'), 500
