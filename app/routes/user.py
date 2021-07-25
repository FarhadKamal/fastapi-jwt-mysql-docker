from fastapi import APIRouter, HTTPException, Depends
from app.config.db import conn
from app.models.index import users
from app.schemas.index import User
from app.schemas.index import AuthDetails
from app.auth import AuthHandler
user =APIRouter()

auth_handler = AuthHandler()


@user.get("/")
async def read_user_data():
 return {"message":"Welcome"} 

@user.get("/users")
async def read_user_data(username=Depends(auth_handler.auth_wrapper)):
 return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id:int,username=Depends(auth_handler.auth_wrapper)):
 return conn.execute(users.select().where(users.c.id == id)).first()


@user.post("/register")
async def write_data(user:User):
  fetch_users=conn.execute(users.select()).fetchall()
  if any(x['username'] == user.username for x in fetch_users):
        raise HTTPException(status_code=400, detail='Username is taken')
  hashed_password = auth_handler.get_password_hash(user.password)
  conn.execute(users.insert().values(
  name=user.name,
  email=user.email,
  
  username=user.username,
  password=hashed_password

 ))
  return conn.execute(users.select()).fetchall()

@user.post('/login')
def login(auth_details: AuthDetails):
    user = None
    fetch_users=conn.execute(users.select()).fetchall()	
    for x in fetch_users:
        if x['username'] == auth_details.username:
            user = x
            break
    
    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user['username'])
    return { 'token': token }


@user.patch("/{id}")
async def update_data(id:int,user:User): 
  hashed_password = auth_handler.get_password_hash(user.password) 
  

  update_data = user.dict(exclude_unset=True)

  conn.execute(users.update().values(
   update_data

  ).where(users.c.id == id))
  return conn.execute(users.select().where(users.c.id == id)).fetchall()


@user.delete("/{id}")
async def read_data(id:int,username=Depends(auth_handler.auth_wrapper)):
  conn.execute(users.delete().where(users.c.id == id))
  return conn.execute(users.select()).fetchall()


