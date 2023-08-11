from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)

class Database:
    def __init__(self, db_url="sqlite:///data.db"):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def store_data(self, data):
        session = self.Session()
        for item in data:
            data_item = Data(name=item['name'], value=item['value'])
            session.add(data_item)
        session.commit()
