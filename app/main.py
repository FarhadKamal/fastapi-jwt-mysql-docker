from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.index import user

# app = FastAPI(docs_url="/documentation", redoc_url=None)
app=FastAPI()

origins = [

    "http://localhost",
    "http://localhost:3000"
  
   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
# @app.get("/")
# def read_sometinng():
#  return{"msg":"hello gadha!"}


