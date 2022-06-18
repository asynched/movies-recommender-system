import pandas as pd, numpy as np, re as regex
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def _clean_title(title: str) -> str:
    return regex.sub(r"[^\w\d\s]", "", title)


class MovieRecommender:
    def __init__(self, movies: str, ratings: str):
        self.m_movies = pd.read_csv(movies)
        self.m_ratings = pd.read_csv(ratings)

        self.__perform_cleanup()
        self.__setup_vectorizer()

    def __perform_cleanup(self):
        """Cleanup the dataset"""
        self.m_movies["clean_title"] = self.m_movies["title"].apply(_clean_title)

    def __setup_vectorizer(self):
        """Sets up the TFIDF vectorizer class"""
        self.m_vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.m_tfidf = self.m_vectorizer.fit_transform(self.m_movies["clean_title"])

    def _get_similar_movies(self, raw_title: str):
        """Gets movies that have similar titles to the one passed in."""
        title = _clean_title(raw_title)
        query_vector = self.m_vectorizer.transform([title])
        similarities = cosine_similarity(query_vector, self.m_tfidf).flatten()
        indices = np.argpartition(similarities, -5)[-5:]

        return self.m_movies.iloc[indices][::-1]

    def _find_recommendations(self, movie_id: int):
        """Find movie recommendations from the title passed in"""
        ratings = self.m_ratings
        movies = self.m_movies

        # Finds the similar user ids to the given movie id that rated the given
        # movie with a rating greater than four.
        similar_users = ratings[
            (ratings["movieId"] == movie_id) & (ratings["rating"] > 4)
        ]["userId"].unique()

        # Finds the movies that have been rated by the similar users.
        similar_user_recs = ratings[
            (ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)
        ]["movieId"]

        # Sets the variable to a percentage of the percentage of total
        # recommendations within the dataset.
        similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

        # Filters the recommendations to get the ones that are greater than
        # the threshold.
        similar_user_recs = similar_user_recs[similar_user_recs > 0.10]

        all_users = ratings[
            (ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)
        ]

        all_user_recs = all_users["movieId"].value_counts() / len(
            all_users["userId"].unique()
        )

        rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
        rec_percentages.columns = ["similar", "all"]
        rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
        rec_percentages = rec_percentages.sort_values("score", ascending=False)

        merged_recs = rec_percentages.head(10).merge(
            movies,
            left_index=True,
            right_on="movieId",
        )

        return merged_recs[["score", "title", "genres"]]

    def get_recommendations(self, title: str):
        similar_movies = self._get_similar_movies(title)
        recommendations = self._find_recommendations(similar_movies.iloc[0]["movieId"])
        return recommendations
