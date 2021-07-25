from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from app.config.db import meta,engine

users = Table(
 'users',meta,
 Column('id',Integer,primary_key=True),
 Column('name',String(30)),
 Column('email',String(30)),
 Column('password',String(255)),
 Column('username',String(20))
)
meta.create_all(engine)