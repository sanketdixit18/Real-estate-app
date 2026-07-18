

# import pickle
# import pandas as pd


# def load_city(city):

#     city = city.lower()

#     # ------------------------
#     # DATASETS
#     # ------------------------

#     analytics_df = pd.read_csv(f"data/{city}/analytics.csv")

#     wordcloud_df = pd.read_csv(f"data/{city}/wordcloud.csv")

#     recommendation_df = pd.read_csv(f"data/{city}/recommendation.csv")

#     market_df = pd.read_csv(f"data/{city}/market_trends.csv")


#     # You are not using Locality Explorer yet
#     locality_df = None

#     # ------------------------
#     # MODELS
#     # ------------------------

#     with open(f"model/{city}/df.pkl", "rb") as f:
#         df = pickle.load(f)

#     with open(f"model/{city}/pipeline.pkl", "rb") as f:
#         pipeline = pickle.load(f)

#     with open(f"model/{city}/recommend_df.pkl", "rb") as f:
#         recommend_df = pickle.load(f)

#     with open(f"model/{city}/hybrid_similarity.pkl", "rb") as f:
#         similarity = pickle.load(f)

#     return (
#         df,
#         pipeline,
#         analytics_df,
#         wordcloud_df,
#         recommendation_df,
#         locality_df,
#         market_df,
#         recommend_df,
#         similarity
#     )


import os
import pickle
import gdown
import pandas as pd


PIPELINE_IDS = {
    "gurgaon": "1JDH4QRm7VoCuT2g_KpHM-Ch33urv9e7g",
    # "mumbai": "ADD_MUMBAI_FILE_ID_HERE"
}


# def download_pipeline(city):
#     pipeline_path = f"model/{city}/pipeline.pkl"

#     if not os.path.exists(pipeline_path):
#         os.makedirs(os.path.dirname(pipeline_path), exist_ok=True)

#         gdown.download(
#             id=PIPELINE_IDS[city],
#             output=pipeline_path,
#             quiet=False
#         )


def download_pipeline(city):
    pipeline_path = f"model/{city}/pipeline.pkl"

    if os.path.exists(pipeline_path):
        return

    os.makedirs(os.path.dirname(pipeline_path), exist_ok=True)

    print(f"Downloading pipeline for {city}...")

    url = f"https://drive.google.com/uc?id={PIPELINE_IDS[city]}"

    output = gdown.download(url, pipeline_path, quiet=False)

    print("Download output:", output)
    print("File exists:", os.path.exists(pipeline_path))

    if not os.path.exists(pipeline_path):
        raise FileNotFoundError(
            f"Failed to download pipeline from Google Drive for {city}."
        )


def load_city(city):

    city = city.lower()

    analytics_df = pd.read_csv(f"data/{city}/analytics.csv")
    wordcloud_df = pd.read_csv(f"data/{city}/wordcloud.csv")
    recommendation_df = pd.read_csv(f"data/{city}/recommendation.csv")
    market_df = pd.read_csv(f"data/{city}/market_trends.csv")

    locality_df = None

    with open(f"model/{city}/df.pkl", "rb") as f:
        df = pickle.load(f)

    # Download pipeline if missing
    download_pipeline(city)

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