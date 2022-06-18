from server.algorithms.movie_recommender import MovieRecommender


class MovieRecommenderFactory:
    __instance: MovieRecommender = None

    @staticmethod
    def get_instance():
        if MovieRecommenderFactory.__instance is None:
            MovieRecommenderFactory.__instance = MovieRecommender(
                "movies.csv",
                "ratings.csv",
            )

        return MovieRecommenderFactory.__instance
