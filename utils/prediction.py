import streamlit as st
import pandas as pd
import numpy as np

def prediction_page(df, pipeline):
    
        st.header("House Price Prediction")
        # Prediction form here
        st.header("Enter your inputs")
        #property types
        # property_type=st.selectbox('Property Type',['Flat','House'])
        property_type = st.selectbox(
            "Property Type",
            sorted(df['property_type'].unique().tolist())
        )
        sector = st.selectbox(
            'Sector',
            sorted(df['sector'].unique().tolist())
        )

        bedrooms = st.selectbox(
            'Bedrooms',
            sorted(df['bedRoom'].unique().tolist())
        )

        bathroom = st.selectbox(
            'Bathrooms',
            sorted(df['bathroom'].unique().tolist())
        )

        balcony = st.selectbox(
            'Balconies',
            sorted(df['balcony'].unique().tolist())
        )

        property_age = st.selectbox(
            'Property Age',
            sorted(df['agePossession'].unique().tolist())
        )

        built_up_area = st.number_input(
            'Built Up Area (sq ft)',
            min_value=100,
            step=50
        )

        servant_room = st.selectbox(
            'Servant Room',
            [0.0,1.0]
        )

        store_room = st.selectbox(
            'Store Room',
            [0.0,1.0]
        )

        furnishing_type = st.selectbox(
            'Furnishing',
            sorted(df['furnishing_type'].unique())
        )

        luxury_category = st.selectbox(
            'Luxury Category',
            sorted(df['luxury_category'].unique())
        )

        floor_category = st.selectbox(
            'Floor Category',
            sorted(df['floor_category'].unique())
        )

        # -------------------------------
        # Prediction
        # -------------------------------

        if st.button("🔮 Predict Price", use_container_width=True):

            # Create input dataframe
            data = [[
                property_type,
                sector,
                bedrooms,
                bathroom,
                balcony,
                property_age,
                built_up_area,
                servant_room,
                store_room,
                furnishing_type,
                luxury_category,
                floor_category
            ]]

            columns = [
                'property_type',
                'sector',
                'bedRoom',
                'bathroom',
                'balcony',
                'agePossession',
                'built_up_area',
                'servant room',
                'store room',
                'furnishing_type',
                'luxury_category',
                'floor_category'
            ]

            input_df = pd.DataFrame(data, columns=columns)

            # Make prediction
            prediction = pipeline.predict(input_df)

            # Convert back from log scale
            predicted_price = np.expm1(prediction)[0]

            # Confidence Range (Approx.)
            error_margin = 0.22          # You can replace this with RMSE later
            lower_price = predicted_price - error_margin
            upper_price = predicted_price + error_margin

            # Prevent negative values
            lower_price = max(lower_price, 0)

            st.divider()

            st.success("✅ Prediction Generated Successfully")

            # Display Metrics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    label="📉 Lower Estimate",
                    value=f"₹ {lower_price:.2f} Cr"
                )

            with col2:
                st.metric(
                    label="🏠 Predicted Price",
                    value=f"₹ {predicted_price:.2f} Cr"
                )

            with col3:
                st.metric(
                    label="📈 Upper Estimate",
                    value=f"₹ {upper_price:.2f} Cr"
                )

            st.info(
                f"""
        ### Estimated Price Range

        🏠 **Your property is estimated to be worth between**

        ## ₹ {lower_price:.2f} Crore — ₹ {upper_price:.2f} Crore

        The estimated market value based on the selected property features is:

        ### **₹ {predicted_price:.2f} Crore**
        """
            )

            # Optional: Show input summary
            with st.expander("📋 View Property Details"):

                st.dataframe(
                    input_df,
                    use_container_width=True,
                    hide_index=True
                )