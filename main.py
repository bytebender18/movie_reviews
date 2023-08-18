from flask import Flask,render_template
from movie_routes import movie_routes
from review_routes import review_routes

app = Flask(__name__)
app.register_blueprint(movie_routes, url_prefix="/movie")
app.register_blueprint(review_routes, url_prefix="/review")

if __name__ == "__main__":
	print("Starting app")
	app.run(port=8080, debug = True)





