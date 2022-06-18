from server.algorithms.movie_recommender import MovieRecommender


class MovieRecommenderService:
    def __init__(self, recommender: MovieRecommender):
        self.m_recommender = recommender

    def get_recommendations(self, title: str) -> list:
        recommendations = self.m_recommender.get_recommendations(title)

        data = []

        for (index, item) in recommendations.iterrows():
            data.append(
                {
                    "id": index,
                    "score": item.score,
                    "title": item.title,
                    "genres": item.genres.split("|"),
                }
            )

        return data
