from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL Connection Configuration
db_user = "root"
db_password = "1234"
db_host = "localhost"
db_port = 3306
db_name = "messages"  

# MySQL Connection URL
db_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create the MySQL Engine
engine = create_engine(db_url)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()









# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# db_name = 'mysql+pymysql://root:1234@localhost:3306/messages'

# engine = create_engine(db_name, connect_args={"check_same_thread": False})

# Base = declarative_base()

# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

 
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
    
#     finally:
#         db.close() 



# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# db_name = "sqlite:///./blog.db"


# engine = create_engine(db_name, connect_args={"check_same_thread": False})

# Base = declarative_base()

# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
 
 
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close() 