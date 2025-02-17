import lightgbm as lgb
from sklearn.preprocessing import StandardScaler
import os
import pickle


def train_model(dataFrame):
    # Separate features and target
    X = dataFrame.drop(columns=['price'])
    y = dataFrame['price']

    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    MODEL_PATH = f"{os.getcwd()}\\models\\scaler.pkl"
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(scaler, f)

    # Create and train the LightGBM model
    model = lgb.LGBMRegressor()
    model.fit(X_scaled, y)

    return model
