# encoding=utf-8
import peewee

db = peewee.MySQLDatabase("my_data", host="localhost", user="root", passwd="111111")


class MySQLModel(peewee.Model):
    class Meta:
        database = db


class Student(MySQLModel):
    name = peewee.CharField(primary_key=True)
    password = peewee.CharField()
    address = peewee.CharField()
    score = peewee.IntegerField()

db.connect()
