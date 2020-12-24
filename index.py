import os
from flask_migrate import Migrate
from dotenv import load_dotenv
from app import create_app, db
from app.models import (
    test
)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# 建立Flask 的 Current App
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# 遷移腳本
migrate = Migrate(app, db)
