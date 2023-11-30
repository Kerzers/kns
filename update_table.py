#!/usr/bin/python3
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://KNS_dev:KNS_dev_pwd@localhost/KNS_dev_db')
Session = sessionmaker(bind=engine)
session = Session()
alter_query = text("ALTER TABLE teachers ADD COLUMN user_email VARCHAR(60) NOT NULL;")
session.execute(alter_query)
alter_query = text("ALTER TABLE teachers ADD COLUMN user_discord VARCHAR(60);")
session.execute(alter_query)
alter_query = text("ALTER TABLE teachers ADD COLUMN user_wtsp VARCHAR(60);")
session.execute(alter_query)
alter_query = text("ALTER TABLE users ADD COLUMN user_discord VARCHAR(60);")
session.execute(alter_query)
alter_query = text("ALTER TABLE users ADD COLUMN user_wtsp VARCHAR(60);")
session.execute(alter_query)
session.commit()
session.close()
