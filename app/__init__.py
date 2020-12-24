import logging
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from configs.config import config
from flask_seeder import FlaskSeeder
from flask_session import Session
from flask_debugtoolbar import DebugToolbarExtension
from flask_marshmallow import Marshmallow
from flask_qrcode import QRcode
from flask_caching import Cache
import logging

# 設定DB的ORM
db = SQLAlchemy()
# 設定登入的方式
login_manager = LoginManager()
# 設凳logging層級
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
# 設定Email
mail = Mail()
# 設定Cache
cache = Cache()
# 設定種子檔
seeder = FlaskSeeder()
# 設定Session
session = Session()
# 驗證用的ma
ma = Marshmallow()
# qrcode
qrcode = QRcode()


def create_app(config_name):
    """初始化APP"""
    app = Flask(__name__)
    # 取得組態物件
    app.config.from_object(config[config_name])
    # 啟用設定檔 開始初始化相關的設定
    config[config_name].init_app(app)
    # 將實例化的app 分派給各個套件
    db.init_app(app)
    # 啟用Flask Login
    login_manager.init_app(app)
    # 啟用Cache
    cache.init_app(app, config={
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_HOST': config[config_name].REDIS_HOST,
        'CACHE_REDIS_PORT': config[config_name].REDIS_PORT,
        'CACHE_REDIS_DB': config[config_name].REDIS_CHANNEL,
        'CACHE_KEY_PREFIX': config[config_name].SECRET_KEY
    })
    # 啟用Mail
    mail.init_app(app)
    # 啟用Seeder
    seeder.init_app(app, db)
    # 啟用Session
    session.init_app(app)
    # 啟用ma
    ma.init_app(app)
    # qrcode
    qrcode.init_app(app)
    # debug bar
    app.debug = config[config_name].DEBUG
    toolbar = DebugToolbarExtension(app)

    # 匯入藍圖
    # 主要網站
    from .views.mains import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Command
    from .commands.tools_cmd import tools as tools_blueprint
    app.register_blueprint(tools_blueprint)

    # 修改轉譯符號
    # app.jinja_env.variable_start_string = '[['
    # app.jinja_env.variable_end_string = ']]'

    return app