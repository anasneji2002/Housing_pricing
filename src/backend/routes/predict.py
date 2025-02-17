import joblib
import os
from sklearn.preprocessing import StandardScaler

from backend.schemas import PredictionRequest, CITY_MAPPING

# Load trained model (update path if needed)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "model.pkl")
SCALER_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "scaler.pkl")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"⚠️ Model not found: {e}")
    model = None

try:
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    print(f"⚠️ scaler not found: {e}")
    scaler = None


def predict_price(request: PredictionRequest):
    """Predict house price based on input features."""
    if model is None or scaler is None:
        raise ValueError("Model or scaler is not loaded. Ensure 'model.pkl' exists.")

    print(request)

    # Convert city name to corresponding ID
    city_id = CITY_MAPPING.get(request.city, 0)  # Default to 0 if not found

    print(f'city_id{city_id}')

    features = [
        request.surface,
        city_id,  # Use city ID instead of name
        request.rooms,
        request.bathrooms,
        request.parking,
        request.pool,
        request.vue_panoramique,
        request.jardin,
        request.climatisation,
        request.chauffage_central,
        request.ascenseur,
    ]

    features_after_normalization = scaler.transform([features])
    prediction = model.predict(features_after_normalization)
    print(prediction)
    return round(prediction[0], 2)
