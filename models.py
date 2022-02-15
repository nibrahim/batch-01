from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, Table, Text
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
# metaclass

class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer, primary_key = True)
    name = Column(String(50))

class Song(Base):
    __tablename__ = "song"
    id = Column(Integer, primary_key = True)
    artist = Column(Integer, ForeignKey('artist.id'))
    artist_obj = relationship("Artist", backref="songs")
    name = Column(String(100))
    lyrics = Column(Text())
    
def get_session(db_url):
    engine = create_engine(db_url)
    Session = sessionmaker(bind = engine)
    session = Session()
    return session
