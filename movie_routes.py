from flask import Blueprint,render_template,jsonify,request
from repositories import movie_repository
from repositories.movie_repository import Movie 


movie_routes = Blueprint('movie_route',__name__)

@movie_routes.route("/add",methods=['POST'])
def movie_info():
	data = request.json
	title = data['title']
	year_released = data['year_released']
	director = data['director']

	movie_repository.save_movie_info(title, year_released, director)

	return jsonify({"message":"Movie Information saved successfully"}), 200


@movie_routes.route("/movies",methods=['GET'])
def all_movies():
	movies = movie_repository.fetch_all_movies()
	return jsonify({"Movies":movies}), 200


@movie_routes.route("/title/<string:title>", methods=['GET'])
def fetch_movie_by_title(title):
	movie = movie_repository.fetch_by_title(title)
	if movie is None:
		return jsonify({"Error":"No title found"}),404
	return jsonify(movie.to_json()),200






