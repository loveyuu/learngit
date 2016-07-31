# encoding=utf-8
import peewee

from mainserver.db import db


class MySQLModel(peewee.Model):
    class Meta:
        database = db


class User(MySQLModel):
    id = peewee.PrimaryKeyField()
    username = peewee.CharField()
    password = peewee.CharField()
