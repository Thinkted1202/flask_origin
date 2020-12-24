from .. import db
from sqlalchemy import inspect


class DBAbstract(db.Model):
    __abstract__ = True

    def object_as_dict(self):
        """將DB Obj轉換為 DICT"""
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

    @staticmethod
    def list_as_dict(table_rows: list, column: list):
        """將DB Obj轉換為 DICT"""
        table_row = []
        for row in table_rows:
            rowdata = {}
            for c in inspect(row).mapper.column_attrs:
                if c.key in column:
                    rowdata[c.key] = getattr(row, c.key)
            table_row.append(rowdata)
        return table_row

    def get_ids(obj):
        result = []
        for row in obj:
            result.append(row.id)
        return row
