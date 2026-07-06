from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://3QUwFTxJispgn9h.root:CDLzjn9DYtFHzLsl@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?ssl=true"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
              "ssl":True
            }
    }
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
