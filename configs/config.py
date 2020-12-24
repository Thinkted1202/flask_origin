import os
import logging
from redis import Redis
from dotenv import load_dotenv

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../')

dotenv_path = os.path.join(basedir, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

logging.info(dotenv_path)


class Config:
    # SECRET KEY 設定
    SECRET_KEY = os.getenv('SECRET_KEY') or 'emc_reddoor'
    # SERVER NAME 設定
    SERVER_NAME = os.getenv('SERVER_NAME')
    # URL SCHEMA
    URL_SCHEMA = os.getenv('URL_SCHEMA') or 'https'
    # Mail 內容設定
    FLASKY_MAIL_SUBJECT_PREFIX = os.getenv('FLASKY_MAIL_SUBJECT_PREFIX')
    FLASKY_MAIL_SENDER = os.getenv('FLASKY_MAIL_SENDER')
    FLASKY_ADMIN = os.getenv('FLASKY_ADMIN')
    # SQLALCHEMY ORM 設定
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_POOL_RECYCLE = 1
    # REDIS 設定
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
    REDIS_CHANNEL = os.getenv('REDIS_CHANNEL')
    # 設定url_for static的版本號
    STATIC_VERSION = '018' or os.getenv('STATIC_VERSION')
    # Google recaptcha
    GOOGLE_CLIENT_RECAPTCHA = os.getenv('GOOGLE_CLIENT_RECAPTCHA')
    GOOGLE_SERVER_RECAPTCHA = os.getenv('GOOGLE_SERVER_RECAPTCHA')
    # Session設定
    SESSION_USE_SIGNER = True
    SESSION_TYPE = "redis"
    SESSION_REDIS = Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'))
    PERMANENT_SESSION_LIFETIME = int(os.getenv('PERMANENT_SESSION_LIFETIME'))

    # 與下面的環境區分出不同的子類別
    @staticmethod
    def init_app(app):
        pass


# 開發環境
class DevelopmentConfig(Config):
    DEBUG = True
    GOOGLE_ANALYTICS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:redd00r@172.18.0.110:3306/emc'
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL') or \
    			'mysql+pymysql://' + os.getenv('DB_ACCOUNT') +':'+ os.getenv('DB_PASSWORD') +'@' +os.getenv('DB_HOST')+':3306/'+os.getenv('DB_NAME')
    # Mail-SMTP Server 設定
    MAIL_SERVER = os.getenv('MAIL_HOST')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_DEBUG = int(os.getenv('MAIL_DEBUG'))
    # 類方法（不需要實例化類就可以被類本身調用）
    @classmethod
    def init_app(cls, app):  # 實做一個init_app的類別 區分不同的環境
        Config.init_app(app)


# 測試環境 SIT
class SitConfig(Config):
    DEBUG = True
    GOOGLE_ANALYTICS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SQLALCHEMY_DATABASE_URI = os.getenv('SIT_DATABASE_URL') or \
                              'mysql+pymysql://' + os.getenv('DB_ACCOUNT') + ':' + os.getenv(
        'DB_PASSWORD') + '@' + os.getenv('DB_HOST') + ':3306/' + os.getenv('DB_NAME')
    # Mail-SMTP Server 設定
    MAIL_SERVER = os.getenv('MAIL_HOST')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_DEBUG = int(os.getenv('MAIL_DEBUG'))

    # 類方法（不需要實例化類就可以被類本身調用）
    @classmethod
    def init_app(cls, app):  # 實做一個init_app的類別 區分不同的環境
        Config.init_app(app)


# 測試環境 UAT
class UatConfig(Config):
    DEBUG = False
    GOOGLE_ANALYTICS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL') or \
                              'mysql+pymysql://' + os.getenv('DB_ACCOUNT') + ':' + os.getenv(
        'DB_PASSWORD') + '@' + os.getenv('DB_HOST') + ':3306/' + os.getenv('DB_NAME')
    # Mail-SMTP Server 設定
    MAIL_SERVER = os.getenv('MAIL_HOST')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', True)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEBUG = int(os.getenv('MAIL_DEBUG'))

    # 類方法（不需要實例化類就可以被類本身調用）
    @classmethod
    def init_app(cls, app):  # 實做一個init_app的類別 區分不同的環境
        Config.init_app(app)


# 正式環境 Production
class ProductionConfig(Config):
    DEBUG = False
    GOOGLE_ANALYTICS = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
                              'mysql+pymysql://' + os.getenv('DB_ACCOUNT') + ':' + os.getenv(
        'DB_PASSWORD') + '@' + os.getenv('DB_HOST') + ':3306/' + os.environ.get('DB_NAME')
    # Mail-SMTP Server 設定
    MAIL_SERVER = os.getenv('MAIL_HOST')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', True)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEBUG = int(os.getenv('MAIL_DEBUG'))

    # 類方法（不需要實例化類就可以被類本身調用）
    @classmethod
    def init_app(cls, app):  # 實做一個init_app的類別 區分不同的環境
        Config.init_app(app)


# Docker的設定檔
class DockerConfig(DevelopmentConfig):
    @classmethod
    def init_app(cls, app):
        DevelopmentConfig.init_app(app)


# 設定預設的環境和其他環境的Object
config = {
    'development': DevelopmentConfig,
    'sit': SitConfig,
    'uat': UatConfig,
    'production': ProductionConfig,
    'docker': DockerConfig,
    'default': DevelopmentConfig
}
