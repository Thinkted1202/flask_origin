from flask_seeder import Seeder
from app.models.test import Test
from datetime import datetime


class SystemSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 9

    # run() will be called by Flask-Seeder
    def run(self):
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Rules
        insert_row = [
            {
                'id': 1,
                'name': '測試用'
            },
            {
                'id': 2,
                'name': '測試用2'
            }
        ]

        for row in insert_row:
            test = Test()
            test.id = row['id']
            test.name = row['name']

            if test.query.get(row['id']) is None:
                print("Adding rules: %s" % row)
                self.db.session.add(test)
            else:
                print("Update rules: %s" % row)
        # ***********************************************