#!/usr/bin/python3
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://KNS_dev:KNS_dev_pwd@localhost/KNS_dev_db')
Session = sessionmaker(bind=engine)
session = Session()
alter_query = text("ALTER TABLE reviews ADD COLUMN username VARCHAR(60) NOT NULL;")
session.execute(alter_query)
session.commit()
session.close()
