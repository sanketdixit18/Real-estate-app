import streamlit as st

from utils.loader import load_city
from utils.prediction import prediction_page
from utils.analytics import analytics_page
from utils.recommendation import recommendation_page
from utils.market_trends import market_trends_page

# -------------------------
# Select City
# -------------------------

st.sidebar.title("🏙 Select City")

city = st.sidebar.selectbox(
    "Choose City",
    [
        "Gurgaon",
        "Mumbai"
    ]
)

# -------------------------
# Load Selected City
# -------------------------

(
    df,
    pipeline,
    analytics_df,
    wordcloud_df,
    recommendation_df,
    locality_df,
    market_df,
    recommend_df,
    similarity
) = load_city(city)




st.title(f"🏠 {city} Real Estate Dashboard")

st.markdown(
    f"Explore **{city}** Real Estate with Prediction, Analytics, Recommendation and Market Trends."
)

st.divider()


# ==========================================
# TABS
# ==========================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Prediction",
    "📊 Analysis",
    "🎯 Recommendation",
    "📈 Market Trends",
    "🗺️ Locality Explorer"
])


# ==========================================
# PREDICTION
# ==========================================

with tab1:
    prediction_page(
        df,
        pipeline
    )


# ==========================================
# ANALYTICS
# ==========================================

with tab2:
    analytics_page(
        analytics_df,
        wordcloud_df
    )


# ==========================================
# RECOMMENDATION
# ==========================================

with tab3:
    recommendation_page(
        recommend_df,
        similarity
    )


# ==========================================
# MARKET TRENDS
# ==========================================

with tab4:
    market_trends_page(
        market_df
    )


# ==========================================
# LOCALITY EXPLORER
# ==========================================

with tab5:
    st.info("Coming Soon...")