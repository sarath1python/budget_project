import sqlalchemy.types as types
from sqlalchemy.dialects.postgresql.base import ischema_names

class CIText(types.Concatenable, types.UserDefinedType):

    def get_col_spec(self):
        return 'CITEXT'

    def bind_processor(self, dialect):
        def process(value):
            return value
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            return value
        return process

ischema_names['citext'] = CIText
