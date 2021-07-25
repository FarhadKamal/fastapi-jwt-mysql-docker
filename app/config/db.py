from sqlalchemy import create_engine, MetaData
# engine = create_engine("sqlite:///name.db") host.docker.internal
engine = create_engine("mysql+pymysql://root:Pass1234@172.20.0.1:3306/test")
meta = MetaData()
conn = engine.connect()
