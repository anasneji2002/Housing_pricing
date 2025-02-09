from pydantic import BaseModel
from typing import Literal

# Define available cities with IDs
CITY_MAPPING = {
    "lac 2": 1, "chotrana 3": 2, "menzah 9": 3, "lac 1": 4, "jardins de carthage": 5,
    "manar 2": 6, "kram": 7, "gammarth": 8, "ain zaghouan sud": 9, "carthage": 10,
    "chotrana 2": 11, "marsa": 12, "la goulette": 13, "menzah": 14, "sidi daoud": 15,
    "soukra": 16, "ain zaghouan": 17, "borj cedria": 18, "menzah 5": 19, "chotrana 1": 20,
}


# Define the request format for predictions
class PredictionRequest(BaseModel):
    surface: float
    city: Literal[*CITY_MAPPING.keys()]  # Restrict city names to predefined list
    rooms: int
    bathrooms: int
    parking: int
    pool: int
    vue_panoramique: int
    jardin: int
    climatisation: int
    chauffage_central: int
    ascenseur: int


# Define response format
class PredictionResponse(BaseModel):
    predicted_price: float
