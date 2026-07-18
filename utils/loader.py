

import pickle
import pandas as pd


def load_city(city):

    city = city.lower()

    # ------------------------
    # DATASETS
    # ------------------------

    analytics_df = pd.read_csv(f"data/{city}/analytics.csv")

    wordcloud_df = pd.read_csv(f"data/{city}/wordcloud.csv")

    recommendation_df = pd.read_csv(f"data/{city}/recommendation.csv")

    market_df = pd.read_csv(f"data/{city}/market_trends.csv")


    # You are not using Locality Explorer yet
    locality_df = None

    # ------------------------
    # MODELS
    # ------------------------

    with open(f"model/{city}/df.pkl", "rb") as f:
        df = pickle.load(f)

    with open(f"model/{city}/pipeline.pkl", "rb") as f:
        pipeline = pickle.load(f)

    with open(f"model/{city}/recommend_df.pkl", "rb") as f:
        recommend_df = pickle.load(f)

    with open(f"model/{city}/hybrid_similarity.pkl", "rb") as f:
        similarity = pickle.load(f)

    return (
        df,
        pipeline,
        analytics_df,
        wordcloud_df,
        recommendation_df,
        locality_df,
        market_df,
        recommend_df,
        similarity
    )