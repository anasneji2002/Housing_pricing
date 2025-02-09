import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("🏡 House Price Prediction")

# Define available cities
CITY_MAPPING = {
    "lac 2": 1, "chotrana 3": 2, "menzah 9": 3, "lac 1": 4, "jardins de carthage": 5,
    "manar 2": 6, "kram": 7, "gammarth": 8, "ain zaghouan sud": 9, "carthage": 10,
    "chotrana 2": 11, "marsa": 12, "la goulette": 13, "menzah": 14, "sidi daoud": 15,
    "soukra": 16, "ain zaghouan": 17, "borj cedria": 18, "menzah 5": 19, "chotrana 1": 20,
    "megrine": 21, "dar fadhal": 22, "ain zaghouan nord": 23, "ariana essoughra": 24,
    "bardo": 25, "omrane": 26, "manar": 27, "ariana ville": 28, "jardins menzah 2": 29,
    "ennasr 2": 30, "ennasr": 31, "ghazela": 32, "tunis": 33, "riadh andalous": 34
}


# Collect input features
surface = st.number_input("Surface (m²)", min_value=10, max_value=5000, value=100)
selected_city = st.selectbox("Select a City", options=list(CITY_MAPPING.keys()))
rooms = st.number_input("Rooms", min_value=1, max_value=20, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=1)
parking = st.checkbox("Parking")
pool = st.checkbox("Pool")
vue_panoramique = st.checkbox("Panoramic View")
jardin = st.checkbox("Garden")
climatisation = st.checkbox("Air Conditioning")
chauffage_central = st.checkbox("Central Heating")
ascenseur = st.checkbox("Elevator")

# Convert booleans to 1/0
features = {
    "surface": surface,
    "city": selected_city,  # Send city name to backend
    "rooms": rooms,
    "bathrooms": bathrooms,
    "parking": int(parking),
    "pool": int(pool),
    "vue_panoramique": int(vue_panoramique),
    "jardin": int(jardin),
    "climatisation": int(climatisation),
    "chauffage_central": int(chauffage_central),
    "ascenseur": int(ascenseur)
}

if st.button("Predict Price"):
    response = requests.post(API_URL, json=features)
    if response.status_code == 200:
        price = response.json()["predicted_price"]
        st.success(f"💰 Predicted Price: {price} TND")
    else:
        st.error("Error: Could not get prediction.")
