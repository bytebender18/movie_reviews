from flask import Blueprint,render_template,jsonify,request
from repositories import review_repository
from repositories.review_repository import Review

review_routes = Blueprint('review_route',__name__)

@review_routes.route("/add",methods=['POST'])
def add_review():
	data = request.json
	author = data['author']
	stars = data['stars']
	movie_id = data['movie_id']

	review = review_repository.save_review_info(author, stars, movie_id)
	return jsonify({"message":"Review Information saved successfully"}), 200


@review_routes.route("/reviews/<string:title>",methods=['GET'])
def get_review(title):
	reviews = review_repository.fetch_review_by_title(title)
	response = []
	for review in reviews:
		response.append(review.to_json())
	if reviews is None:
		return jsonify({"Error":"No title found"}),404
	return jsonify(response),200
