from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql://:@localhost/postgres'
engine = create_engine(DATABASE_URL)

metadata = MetaData()
metadata.reflect(engine)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base(metadata=metadata)


class Movie(Base):
    __tablename__ = 'movie'

    def __init__(self, title, year_released, director):
        self.title = title
        self.year_released = year_released
        self.director = director


    def to_json(self):
        return {
        'id' : self.movie_id,
        'title': self.title,
        'year_released': self.year_released,
        'director': self.director
        }

Movie.__table__ = Table('movie', metadata, autoload=True, autoload_with=engine)

def save_movie_info(title, year_released, director):
    movie = Movie(title=title,year_released=year_released,director=director)
    session.add(movie)
    session.commit()
    return movie

def fetch_all_movies():
    all_movies = session.query(Movie).all()
    response = []
    for movie in all_movies:
        response.append(movie.to_json())
    return response

def fetch_by_title(title):
    movie  = session.query(Movie).filter_by(title=title).first()
    if movie is None:
        return None
    return movie














