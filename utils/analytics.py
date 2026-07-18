# import streamlit as st
# import plotly.express as px
# import plotly.graph_objects as go
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud
# import ast

# def analytics_page(analytics_df, wordcloud_df):
#     with tab2:

#         st.title("🌍 Gurgaon Analytics Dashboard")

#         geo_tab, wordcloud_tab, scatter_tab, pie_tab, box_tab, property_tab = st.tabs([
#             "🗺️ Geo Map",
#             "☁️ Word Cloud",
#             "📈 Area vs Price",
#             "🥧 BHK Distribution",
#             "📦 Bedroom Price",
#             "📊 Property Type"
#         ])

#         # -------------------------------
#         # GEO MAP
#         # -------------------------------

#         # -------------------------------
#         # GEO MAP
#         # -------------------------------
#         with geo_tab:

            

#             # ======================================================
#             # KPI CARDS
#             # ======================================================

#             avg_price = analytics_df["price"].mean()
#             max_price = analytics_df["price"].max()
#             min_price = analytics_df["price"].min()
#             total_sectors = analytics_df["sector"].nunique()
#             total_properties = len(analytics_df)

#             col1, col2, col3, col4 = st.columns(4)

#             col1.metric("🏠 Avg Price", f"₹ {avg_price:.1f} Cr")
#             col2.metric("📈 Highest", f"₹ {max_price:.1f} Cr")
#             col3.metric("📉 Lowest", f"₹ {min_price:.3f} Cr")
#             col4.metric("📍 Sectors", total_sectors)
#             # col5.metric("🏢 Listings", total_properties)

#             st.divider()

#             # ======================================================
#             # LAYOUT
#             # ======================================================

#             left, right = st.columns([1, 3])

#             # ======================================================
#             # FILTERS
#             # ======================================================

#             with left:

#                 st.subheader("🎛️ Filters")

#                 selected_sector = st.selectbox(
#                     "Sector",
#                     ["All"] + sorted(analytics_df["sector"].unique())
#                 )

#                 price_range = st.slider(
#                     "Price Range (Cr)",
#                     min_value=float(analytics_df["price"].min()),
#                     max_value=float(analytics_df["price"].max()),
#                     value=(
#                         float(analytics_df["price"].min()),
#                         float(analytics_df["price"].max())
#                     )
#                 )

#             # ======================================================
#             # APPLY FILTERS
#             # ======================================================

#             filtered_df = analytics_df.copy()

#             if selected_sector != "All":
#                 filtered_df = filtered_df[
#                     filtered_df["sector"] == selected_sector
#                 ]

#             filtered_df = filtered_df[
#                 (filtered_df["price"] >= price_range[0]) &
#                 (filtered_df["price"] <= price_range[1])
#             ]

#             # ======================================================
#             # CREATE MAP DATA
#             # ======================================================

#             map_df = (
#                 filtered_df
#                 .groupby("sector", as_index=False)
#                 .agg({
#                     "price": "mean",
#                     "latitude": "first",
#                     "longitude": "first"
#                 })
#             )

#             # ======================================================
#             # RIGHT PANEL
#             # ======================================================

#             with right:

#                 st.subheader("🗺️ Gurgaon Property Price Map")

#                 fig = go.Figure()

#                 fig.add_trace(

#                     go.Scattermapbox(

#                         lat=map_df["latitude"],

#                         lon=map_df["longitude"],

#                         mode="markers",

#                         text=map_df["sector"],

#                         customdata=map_df[["price"]],

#                         marker=dict(

#                             size=18,

#                             color=map_df["price"],

#                             colorscale="Turbo",

#                             showscale=True,

#                             opacity=0.85,

#                             colorbar=dict(
#                                 title="Avg Price (Cr)"
#                             )
#                         ),

#                         hovertemplate=

#                         "<b>%{text}</b><br><br>" +

#                         "Average Price : ₹ %{customdata[0]:.2f} Cr" +

#                         "<extra></extra>"
#                     )
#                 )

#                 fig.update_layout(

#                     mapbox=dict(

#                         style="carto-positron",

#                         center=dict(

#                             lat=28.4595,

#                             lon=77.0266

#                         ),

#                         zoom=10

#                     ),

#                     height=550,

#                     margin=dict(

#                         l=0,

#                         r=0,

#                         t=0,

#                         b=0

#                     )
#                 )

#                 st.plotly_chart(
#                     fig,
#                     use_container_width=True
#                 )


#         # -------Word Cloud----------
#         with wordcloud_tab:
#             st.header("☁️ Amenities Word Cloud")
#             selected_sector = st.selectbox(
#                 "Select Sector",
#                 ["All"] + sorted(wordcloud_df["sector"].unique())
#             )
#             filtered_df = wordcloud_df.copy()

#             if selected_sector != "All":
#                 filtered_df = filtered_df[
#                     filtered_df["sector"] == selected_sector
#                 ]

#             all_features = []

#             for item in filtered_df["features"]:

#                 try:
#                     feature_list = ast.literal_eval(item)
#                     all_features.extend(feature_list)
#                 except:
#                     pass
#             text = " ".join(all_features)
#             wc = WordCloud(
#                 width=1200,
#                 height=600,
#                 background_color="white",
#                 colormap="viridis"
#             ).generate(text)  
#             fig, ax = plt.subplots(figsize=(14,7))

#             ax.imshow(wc)

#             ax.axis("off")

#             st.pyplot(fig) 



#         # --------Area v/s Price Distribution------------
#         with scatter_tab:
#             st.header("📈 Area vs Price Analysis")
#             st.caption("Relationship between Built-up Area and Property Price")
#             col1, col2 = st.columns(2)

#             with col1:

#                 property_type = st.selectbox(
#                     "Property Type",
#                     ["All"] + sorted(analytics_df["property_type"].unique())
#                 )

#             with col2:

#                 bedrooms = st.selectbox(
#                     "Bedrooms",
#                     ["All"] + sorted(analytics_df["bedRoom"].unique().tolist())
#                 )
            
#             filtered = analytics_df.copy()

#             if property_type != "All":
#                 filtered = filtered[
#                     filtered["property_type"] == property_type
#                 ]

#             if bedrooms != "All":
#                 filtered = filtered[
#                     filtered["bedRoom"] == bedrooms
#                 ]

#             import plotly.express as px

#             fig = px.scatter(
#                 filtered,

#                 x="built_up_area",

#                 y="price",

#                 color="property_type",

#                 size="bedRoom",

#                 hover_name="sector",

#                 hover_data={
#                     "built_up_area": True,
#                     "price": ":.2f",
#                     "bedRoom": True
#                 },

#                 height=650
#             )

#             fig.update_layout(

#                 template="plotly_dark",

#                 xaxis_title="Built-up Area (sq ft)",

#                 yaxis_title="Price (Crore ₹)",

#                 title="Area vs Property Price",

#                 legend_title="Property Type"
#             )

#             st.plotly_chart(
#                 fig,
#                 use_container_width=True
#             )




#         # -----------BHK DISTRIBUTION--------------
#         with pie_tab:

#             st.header("🛏 Bedroom Distribution")

#             # ======================================
#             # FILTER
#             # ======================================

#             selected_sector_pie = st.selectbox(
#                 "📍 Select Sector",
#                 ["All"] + sorted(analytics_df["sector"].unique()),
#                 key="pie_sector"
#             )

#             # Apply Sector Filter
#             if selected_sector_pie == "All":
#                 pie_df = analytics_df.copy()
#             else:
#                 pie_df = analytics_df[
#                     analytics_df["sector"] == selected_sector_pie
#                 ].copy()

#             # Check if data exists
#             if pie_df.empty:
#                 st.warning("No properties found for the selected sector.")
#                 st.stop()

#             # ======================================
#             # KPI CARDS
#             # ======================================

#             col1, col2, col3, col4 = st.columns(4)

#             col1.metric(
#                 "🏆 Most Common",
#                 f"{pie_df['bedRoom'].mode()[0]} BHK"
#             )

#             col2.metric(
#                 "🏠 Total Properties",
#                 len(pie_df)
#             )

#             col3.metric(
#                 "📊 Avg Price",
#                 f"₹ {pie_df['price'].mean():.2f} Cr"
#             )

#             col4.metric(
#                 "🔢 Bedroom Types",
#                 pie_df["bedRoom"].nunique()
#             )

#             st.divider()

#             # ======================================
#             # COUNT BEDROOMS
#             # ======================================

#             bhk_count = (
#                 pie_df["bedRoom"]
#                 .value_counts()
#                 .sort_index()
#                 .reset_index()
#             )

#             bhk_count.columns = ["Bedroom", "Count"]

#             # ======================================
#             # LAYOUT
#             # ======================================

#             left, right = st.columns([2, 1])

#             # ======================================
#             # PIE CHART
#             # ======================================

#             with left:

#                 fig = px.pie(

#                     bhk_count,

#                     names="Bedroom",

#                     values="Count",

#                     hole=0.55,

#                     color="Bedroom",

#                     color_discrete_sequence=px.colors.qualitative.Set3
#                 )

#                 fig.update_traces(

#                     textposition="inside",

#                     textinfo="percent+label",

#                     hovertemplate=
#                     "<b>%{label} BHK</b><br>" +
#                     "Properties : %{value}<br>" +
#                     "Percentage : %{percent}<extra></extra>"
#                 )

#                 fig.update_layout(

#                     title=f"Bedroom Distribution ({selected_sector_pie})",

#                     height=550,

#                     showlegend=True
#                 )

#                 st.plotly_chart(
#                     fig,
#                     use_container_width=True
#                 )

#             # ======================================
#             # BEDROOM STATS
#             # ======================================

#             with right:

#                 st.subheader("📋 BHK Summary")

#                 bhk_stats = (
#                     pie_df
#                     .groupby("bedRoom")
#                     .agg(
#                         Properties=("bedRoom", "count"),
#                         Avg_Price=("price", "mean")
#                     )
#                     .reset_index()
#                 )

#                 bhk_stats["Avg_Price"] = bhk_stats["Avg_Price"].round(2)

#                 st.dataframe(
#                     bhk_stats,
#                     hide_index=True,
#                     use_container_width=True,
#                     height=350
#                 )

#                 st.divider()

#                 st.subheader("🏆 Most Popular")

#                 top = bhk_stats.sort_values(
#                     "Properties",
#                     ascending=False
#                 ).iloc[0]

#                 st.success(
#                     f"""
#                     **{int(top['bedRoom'])} BHK**

#                     {int(top['Properties'])} Properties

#                     Avg Price

#                     ₹ {top['Avg_Price']:.2f} Cr
#                     """
#                 )


#         # -------Bedroom Box plate ---------
#         with box_tab:

#             st.header("📦 Bedroom Price Analysis")

#             st.caption(
#                 "Distribution of property prices across different bedroom categories."
#             )
#             selected_sector_box = st.selectbox(
#                 "📍 Select Sector",
#                 ["All"] + sorted(analytics_df["sector"].unique()),
#                 key="box_sector"
#             )

#             if selected_sector_box == "All":
#                 box_df = analytics_df.copy()
#             else:
#                 box_df = analytics_df[
#                     analytics_df["sector"] == selected_sector_box
#                 ].copy()

#             if box_df.empty:
#                 st.warning("No properties found.")
#                 st.stop()
            
#             col1, col2, col3 = st.columns(3)

#             col1.metric(
#                 "🏠 Total Properties",
#                 len(box_df)
#             )

#             col2.metric(
#                 "📊 Average Price",
#                 f"₹ {box_df['price'].mean():.2f} Cr"
#             )

#             col3.metric(
#                 "🛏 Bedroom Types",
#                 box_df["bedRoom"].nunique()
#             )

#             st.divider()

#             fig = px.box(

#                 box_df,

#                 x="bedRoom",

#                 y="price",

#                 color="bedRoom",

#                 points="outliers",

#                 color_discrete_sequence=px.colors.qualitative.Set3
#             )

#             fig.update_layout(

#                 title="Bedroom vs Property Price",

#                 xaxis_title="Bedrooms",

#                 yaxis_title="Price (Crore ₹)",

#                 height=650
#             )
#             fig.update_traces(

#                 hovertemplate=

#                 "<b>%{x} BHK</b><br>" +

#                 "Price : ₹ %{y:.2f} Cr<extra></extra>"
#             )

#             st.plotly_chart(
#                 fig,
#                 use_container_width=True
#             )


#             st.subheader("📋 Price Summary")

#             summary = (

#                 box_df

#                 .groupby("bedRoom")

#                 .agg(

#                     Minimum=("price","min"),

#                     Median=("price","median"),

#                     Average=("price","mean"),

#                     Maximum=("price","max")

#                 )

#                 .round(2)

#                 .reset_index()
#             )

#             st.dataframe(
#                 summary,
#                 use_container_width=True,
#                 hide_index=True
#             )


#         # -----------PROPERTY TYPE------------  
#         with property_tab:

#             st.header("📊 Price Distribution Analysis")

#             # ======================================
#             # FILTER
#             # ======================================

#             selected_sector_hist = st.selectbox(
#                 "📍 Select Sector",
#                 ["All"] + sorted(analytics_df["sector"].unique()),
#                 key="hist_sector"
#             )

#             if selected_sector_hist == "All":
#                 hist_df = analytics_df.copy()
#             else:
#                 hist_df = analytics_df[
#                     analytics_df["sector"] == selected_sector_hist
#                 ].copy()

#             if hist_df.empty:
#                 st.warning("No properties found.")
#                 st.stop()

#             # ======================================
#             # KPI CARDS
#             # ======================================

#             c1, c2, c3, c4 = st.columns(4)

#             c1.metric(
#                 "Average Price",
#                 f"₹ {hist_df['price'].mean():.2f} Cr"
#             )

#             c2.metric(
#                 "Median Price",
#                 f"₹ {hist_df['price'].median():.2f} Cr"
#             )

#             c3.metric(
#                 "Maximum Price",
#                 f"₹ {hist_df['price'].max():.2f} Cr"
#             )

#             c4.metric(
#                 "Properties",
#                 len(hist_df)
#             )

#             st.divider()

#             # ======================================
#             # HISTOGRAM
#             # ======================================

#             fig = px.histogram(

#                 hist_df,

#                 x="price",

#                 nbins=40,

#                 marginal="box",

#                 opacity=0.8,

#                 color_discrete_sequence=["#4F46E5"]

#             )

#             fig.update_layout(

#                 title="Property Price Distribution",

#                 xaxis_title="Price (Crore ₹)",

#                 yaxis_title="Number of Properties",

#                 height=600

#             )

#             st.plotly_chart(
#                 fig,
#                 use_container_width=True
#             )

#             # ======================================
#             # SUMMARY TABLE
#             # ======================================

#             st.subheader("📋 Statistical Summary")

#             summary = hist_df["price"].describe().round(2)

#             st.dataframe(
#                 summary.to_frame().T,
#                 use_container_width=True,
#                 hide_index=True
#             )




import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import ast


def analytics_page(analytics_df, wordcloud_df):
    
        st.title("🌍 Gurgaon Analytics Dashboard")

        geo_tab, wordcloud_tab, scatter_tab, pie_tab, box_tab, property_tab = st.tabs([
            "🗺️ Geo Map",
            "☁️ Word Cloud",
            "📈 Area vs Price",
            "🥧 BHK Distribution",
            "📦 Bedroom Price",
            "📊 Property Type",
        ])

        # -------------------------------
        # GEO MAP
        # -------------------------------
        with geo_tab:

            # ======================================================
            # KPI CARDS
            # ======================================================
            avg_price = analytics_df["price"].mean()
            max_price = analytics_df["price"].max()
            min_price = analytics_df["price"].min()
            total_sectors = analytics_df["sector"].nunique()
            total_properties = len(analytics_df)

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("🏠 Avg Price", f"₹ {avg_price:.1f} Cr")
            col2.metric("📈 Highest", f"₹ {max_price:.1f} Cr")
            col3.metric("📉 Lowest", f"₹ {min_price:.3f} Cr")
            col4.metric("📍 Sectors", total_sectors)
            # col5.metric("🏢 Listings", total_properties)

            st.divider()

            # ======================================================
            # LAYOUT
            # ======================================================
            left, right = st.columns([1, 3])

            # ======================================================
            # FILTERS
            # ======================================================
            with left:
                st.subheader("🎛️ Filters")

                selected_sector = st.selectbox(
                    "Sector",
                    ["All"] + sorted(analytics_df["sector"].unique())
                )

                price_range = st.slider(
                    "Price Range (Cr)",
                    min_value=float(analytics_df["price"].min()),
                    max_value=float(analytics_df["price"].max()),
                    value=(
                        float(analytics_df["price"].min()),
                        float(analytics_df["price"].max())
                    )
                )

            # ======================================================
            # APPLY FILTERS
            # ======================================================
            filtered_df = analytics_df.copy()

            if selected_sector != "All":
                filtered_df = filtered_df[filtered_df["sector"] == selected_sector]

            filtered_df = filtered_df[
                (filtered_df["price"] >= price_range[0]) &
                (filtered_df["price"] <= price_range[1])
            ]

            # ======================================================
            # CREATE MAP DATA
            # ======================================================
            map_df = (
                filtered_df
                .groupby("sector", as_index=False)
                .agg({
                    "price": "mean",
                    "latitude": "first",
                    "longitude": "first"
                })
            )

            # ======================================================
            # RIGHT PANEL
            # ======================================================
            with right:
                st.subheader("🗺️ Gurgaon Property Price Map")

                fig = go.Figure()

                fig.add_trace(
                    go.Scattermapbox(
                        lat=map_df["latitude"],
                        lon=map_df["longitude"],
                        mode="markers",
                        text=map_df["sector"],
                        customdata=map_df[["price"]],
                        marker=dict(
                            size=18,
                            color=map_df["price"],
                            colorscale="Turbo",
                            showscale=True,
                            opacity=0.85,
                            colorbar=dict(title="Avg Price (Cr)")
                        ),
                        hovertemplate=(
                            "<b>%{text}</b><br><br>"
                            "Average Price : ₹ %{customdata[0]:.2f} Cr"
                            "<extra></extra>"
                        )
                    )
                )

                fig.update_layout(
                    mapbox=dict(
                        style="carto-positron",
                        center=dict(lat=28.4595, lon=77.0266),
                        zoom=10
                    ),
                    height=550,
                    margin=dict(l=0, r=0, t=0, b=0)
                )

                st.plotly_chart(fig, use_container_width=True)

        # -------------------------------
        # WORD CLOUD
        # -------------------------------
        with wordcloud_tab:
            st.header("☁️ Amenities Word Cloud")

            selected_sector = st.selectbox(
                "Select Sector",
                ["All"] + sorted(wordcloud_df["sector"].unique())
            )

            filtered_df = wordcloud_df.copy()

            if selected_sector != "All":
                filtered_df = filtered_df[filtered_df["sector"] == selected_sector]

            all_features = []
            for item in filtered_df["features"]:
                try:
                    feature_list = ast.literal_eval(item)
                    all_features.extend(feature_list)
                except Exception:
                    pass

            text = " ".join(all_features)

            wc = WordCloud(
                width=1200,
                height=600,
                background_color="white",
                colormap="viridis"
            ).generate(text)

            fig, ax = plt.subplots(figsize=(14, 7))
            ax.imshow(wc)
            ax.axis("off")

            st.pyplot(fig)

        # -------------------------------
        # AREA VS PRICE DISTRIBUTION
        # -------------------------------
        with scatter_tab:
            st.header("📈 Area vs Price Analysis")
            st.caption("Relationship between Built-up Area and Property Price")

            col1, col2 = st.columns(2)

            with col1:
                property_type = st.selectbox(
                    "Property Type",
                    ["All"] + sorted(analytics_df["property_type"].unique())
                )

            with col2:
                bedrooms = st.selectbox(
                    "Bedrooms",
                    ["All"] + sorted(analytics_df["bedRoom"].unique().tolist())
                )

            filtered = analytics_df.copy()

            if property_type != "All":
                filtered = filtered[filtered["property_type"] == property_type]

            if bedrooms != "All":
                filtered = filtered[filtered["bedRoom"] == bedrooms]

            fig = px.scatter(
                filtered,
                x="built_up_area",
                y="price",
                color="property_type",
                size="bedRoom",
                hover_name="sector",
                hover_data={
                    "built_up_area": True,
                    "price": ":.2f",
                    "bedRoom": True
                },
                height=650
            )

            fig.update_layout(
                template="plotly_dark",
                xaxis_title="Built-up Area (sq ft)",
                yaxis_title="Price (Crore ₹)",
                title="Area vs Property Price",
                legend_title="Property Type"
            )

            st.plotly_chart(fig, use_container_width=True)

        # -------------------------------
        # BHK DISTRIBUTION
        # -------------------------------
        with pie_tab:
            st.header("🛏 Bedroom Distribution")

            # ======================================
            # FILTER
            # ======================================
            selected_sector_pie = st.selectbox(
                "📍 Select Sector",
                ["All"] + sorted(analytics_df["sector"].unique()),
                key="pie_sector"
            )

            if selected_sector_pie == "All":
                pie_df = analytics_df.copy()
            else:
                pie_df = analytics_df[analytics_df["sector"] == selected_sector_pie].copy()

            if pie_df.empty:
                st.warning("No properties found for the selected sector.")
                st.stop()

            # ======================================
            # KPI CARDS
            # ======================================
            col1, col2, col3, col4 = st.columns(4)

            col1.metric("🏆 Most Common", f"{pie_df['bedRoom'].mode()[0]} BHK")
            col2.metric("🏠 Total Properties", len(pie_df))
            col3.metric("📊 Avg Price", f"₹ {pie_df['price'].mean():.2f} Cr")
            col4.metric("🔢 Bedroom Types", pie_df["bedRoom"].nunique())

            st.divider()

            # ======================================
            # COUNT BEDROOMS
            # ======================================
            bhk_count = (
                pie_df["bedRoom"]
                .value_counts()
                .sort_index()
                .reset_index()
            )
            bhk_count.columns = ["Bedroom", "Count"]

            # ======================================
            # LAYOUT
            # ======================================
            left, right = st.columns([2, 1])

            # ======================================
            # PIE CHART
            # ======================================
            with left:
                fig = px.pie(
                    bhk_count,
                    names="Bedroom",
                    values="Count",
                    hole=0.55,
                    color="Bedroom",
                    color_discrete_sequence=px.colors.qualitative.Set3
                )

                fig.update_traces(
                    textposition="inside",
                    textinfo="percent+label",
                    hovertemplate=(
                        "<b>%{label} BHK</b><br>"
                        "Properties : %{value}<br>"
                        "Percentage : %{percent}<extra></extra>"
                    )
                )

                fig.update_layout(
                    title=f"Bedroom Distribution ({selected_sector_pie})",
                    height=550,
                    showlegend=True
                )

                st.plotly_chart(fig, use_container_width=True)

            # ======================================
            # BEDROOM STATS
            # ======================================
            with right:
                st.subheader("📋 BHK Summary")

                bhk_stats = (
                    pie_df
                    .groupby("bedRoom")
                    .agg(
                        Properties=("bedRoom", "count"),
                        Avg_Price=("price", "mean")
                    )
                    .reset_index()
                )
                bhk_stats["Avg_Price"] = bhk_stats["Avg_Price"].round(2)

                st.dataframe(
                    bhk_stats,
                    hide_index=True,
                    use_container_width=True,
                    height=350
                )

                st.divider()

                st.subheader("🏆 Most Popular")

                top = bhk_stats.sort_values("Properties", ascending=False).iloc[0]

                st.success(
                    f"""
                    **{int(top['bedRoom'])} BHK**

                    {int(top['Properties'])} Properties

                    Avg Price

                    ₹ {top['Avg_Price']:.2f} Cr
                    """
                )

        # -------------------------------
        # BEDROOM BOX PLOT
        # -------------------------------
        with box_tab:
            st.header("📦 Bedroom Price Analysis")
            st.caption("Distribution of property prices across different bedroom categories.")

            selected_sector_box = st.selectbox(
                "📍 Select Sector",
                ["All"] + sorted(analytics_df["sector"].unique()),
                key="box_sector"
            )

            if selected_sector_box == "All":
                box_df = analytics_df.copy()
            else:
                box_df = analytics_df[analytics_df["sector"] == selected_sector_box].copy()

            if box_df.empty:
                st.warning("No properties found.")
                st.stop()

            col1, col2, col3 = st.columns(3)

            col1.metric("🏠 Total Properties", len(box_df))
            col2.metric("📊 Average Price", f"₹ {box_df['price'].mean():.2f} Cr")
            col3.metric("🛏 Bedroom Types", box_df["bedRoom"].nunique())

            st.divider()

            fig = px.box(
                box_df,
                x="bedRoom",
                y="price",
                color="bedRoom",
                points="outliers",
                color_discrete_sequence=px.colors.qualitative.Set3
            )

            fig.update_layout(
                title="Bedroom vs Property Price",
                xaxis_title="Bedrooms",
                yaxis_title="Price (Crore ₹)",
                height=650
            )

            fig.update_traces(
                hovertemplate=(
                    "<b>%{x} BHK</b><br>"
                    "Price : ₹ %{y:.2f} Cr<extra></extra>"
                )
            )

            st.plotly_chart(fig, use_container_width=True)

            st.subheader("📋 Price Summary")

            summary = (
                box_df
                .groupby("bedRoom")
                .agg(
                    Minimum=("price", "min"),
                    Median=("price", "median"),
                    Average=("price", "mean"),
                    Maximum=("price", "max")
                )
                .round(2)
                .reset_index()
            )

            st.dataframe(summary, use_container_width=True, hide_index=True)

        # -------------------------------
        # PROPERTY TYPE / PRICE HISTOGRAM
        # -------------------------------
        with property_tab:
            st.header("📊 Price Distribution Analysis")

            # ======================================
            # FILTER
            # ======================================
            selected_sector_hist = st.selectbox(
                "📍 Select Sector",
                ["All"] + sorted(analytics_df["sector"].unique()),
                key="hist_sector"
            )

            if selected_sector_hist == "All":
                hist_df = analytics_df.copy()
            else:
                hist_df = analytics_df[analytics_df["sector"] == selected_sector_hist].copy()

            if hist_df.empty:
                st.warning("No properties found.")
                st.stop()

            # ======================================
            # KPI CARDS
            # ======================================
            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Average Price", f"₹ {hist_df['price'].mean():.2f} Cr")
            c2.metric("Median Price", f"₹ {hist_df['price'].median():.2f} Cr")
            c3.metric("Maximum Price", f"₹ {hist_df['price'].max():.2f} Cr")
            c4.metric("Properties", len(hist_df))

            st.divider()

            # ======================================
            # HISTOGRAM
            # ======================================
            fig = px.histogram(
                hist_df,
                x="price",
                nbins=40,
                marginal="box",
                opacity=0.8,
                color_discrete_sequence=["#4F46E5"]
            )

            fig.update_layout(
                title="Property Price Distribution",
                xaxis_title="Price (Crore ₹)",
                yaxis_title="Number of Properties",
                height=600
            )

            st.plotly_chart(fig, use_container_width=True)

            # ======================================
            # SUMMARY TABLE
            # ======================================
            st.subheader("📋 Statistical Summary")

            summary = hist_df["price"].describe().round(2)

            st.dataframe(
                summary.to_frame().T,
                use_container_width=True,
                hide_index=True
            )