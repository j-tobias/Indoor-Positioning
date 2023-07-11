import pandas as pd
import pickle as pkl
from sklearn.ensemble import RandomForestClassifier

def predict_room(s001, s002, s003, s004, s005) -> int:
    """
    This function maps the Sensor Data of the 5 Sensors to the Room
    """
    
    # Load the trained Random Forest model from file
    with open('models/rf_model.pkl', 'rb') as file:
        rfc = pkl.load(file)

    # Create a DataFrame with the input features
    input_df = pd.DataFrame([[s001, s002, s003, s004, s005]], columns=['s001', 's002', 's003', 's004', 's005'])

    # Make the prediction using the trained Random Forest model
    prediction = rfc.predict(input_df)[0]

    # Return the predicted room
    return prediction

