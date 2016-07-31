# encoding=utf-8
from playhouse.pool import PooledMySQLDatabase


db = PooledMySQLDatabase(
    'any_time',
    max_connections=32,
    stale_timeout=300,  # 5 minutes.
    host="192.168.100.243",
    user="root",
    passwd="abcd.1234")

db.connect()
