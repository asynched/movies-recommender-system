from flask import Flask, jsonify, request
from flask_cors import CORS

from server.factories.movie_recommender import MovieRecommenderFactory
from server.services.movie_recommender import MovieRecommenderService

app = Flask(__name__)
CORS(app)

recommender = MovieRecommenderFactory.get_instance()


@app.get("/recs")
def get_recommendations():
    title = request.args.get("title")

    if title is None:
        return (
            jsonify(
                {
                    "error": "'title' is required",
                }
            ),
            400,
        )

    service = MovieRecommenderService(recommender)
    data = service.get_recommendations(title)

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(port=8081, debug=True)
