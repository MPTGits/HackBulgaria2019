class BaseModelMetaclass(type):
    pass


class Column:
    #constrains=()

    def __init__(self,name,unique=False):
        self.name=name
        self.unique=unique

    def as_sql(self):
        #=> ID INTEGER PRIMARY KEY AUTOINCREMENT
        constrains_str=self.get_constrains()
        unique_str=self.unique and 'UNIQUE' or ''
        return f'{self.name} {self.column_type} {constrains_str} {unique_str}'

    def get_constrains(self):
        return ''.join(self.constrains)


class PKColumn():
    column_type='INTEGER'

    constrains_type=(
        'PRIMARY KEY',
        'AUTOINCREMENT'
        )

    def __init__(self):
        pass

class TextColumn(Column):

    column_type='Text'

    def __init__(self,name):
        super().__init__(name)


class Basemodel(metaclass=BaseModelMetaclass):
    id=PKColumn()