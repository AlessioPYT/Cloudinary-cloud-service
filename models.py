from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PhotoLink(Base):
    __tablename__ = 'photo_links'
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    transformed_url = Column(String, nullable=False)
    qr_code_url = Column(String, nullable=False)

