from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from repositories import movie_repository
from repositories.movie_repository import Movie 

DATABASE_URL = 'postgresql://:@localhost/postgres'
engine = create_engine(DATABASE_URL)

metadata = MetaData()
metadata.reflect(engine)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base(metadata=metadata)

class Review(Base):
	__tablename__ = 'review'

	def __init__(self, author, stars, movie_id):
		self.author = author
		self.stars = stars
		self.movie_id = movie_id

	def to_json(self):
		return {
		'id' : self.review_id,
		'author' : self.author,
		'stars' : self.stars,
		'movie_id' : self.movie_id
		}


Review.__table__ = Table('review', metadata, autoload=True, autoload_with=engine)


def save_review_info(author,stars,movie_id):
	review = Review(author=author,stars=stars,movie_id=movie_id)
	session.add(review)
	session.commit()
	return review

def fetch_review_by_title(title):
	movie = movie_repository.fetch_by_title(title)
	reviews = session.query(Review).filter_by(movie_id = movie.movie_id).all()
	return reviews



