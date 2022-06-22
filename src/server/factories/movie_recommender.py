import joblib, os
from server.algorithms.movie_recommender import MovieRecommender

class MovieRecommenderFactory:
    __instance: MovieRecommender = None

    @staticmethod
    def get_instance():
        if os.path.exists('ml-model.save'):
            MovieRecommenderFactory.__instance = joblib.load('ml-model.save')

        if MovieRecommenderFactory.__instance is None:
            MovieRecommenderFactory.__instance = MovieRecommender(
                "movies.csv",
                "ratings.csv",
            )
            joblib.dump(MovieRecommenderFactory.__instance, 'ml-model.save')

        return MovieRecommenderFactory.__instance
