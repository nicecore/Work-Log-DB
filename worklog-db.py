from peewee import *
import datetime

db = SqliteDatabase('employees.db')

class Employee(Model):
    name = CharField(max_length=255, unique=True)
    task_name = CharField(max_length=255)
    time = DateTimeField(default=datetime.datetime.now)
    minutes = IntegerField(default=0)
    notes = TextField()

    class Meta:
        database = db


if __name__ == '__main__':
    db.connect()
    db.create_tables([Employee], safe=True)