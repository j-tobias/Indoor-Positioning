import pandas as pd
import pickle as pkl
from sklearn.ensemble import RandomForestClassifier

def predict_room(Sensors) -> int:
    """
    This function maps the Sensor Data of the 5 Sensors to the Room
    """
    
    # Load the trained Random Forest model from file
    with open('models/rf_model.pkl', 'rb') as file:
        rfc = pkl.load(file)

    # Create a DataFrame with the input features
    input_df = pd.DataFrame([[Sensors[key] for key in sorted(Sensors)]], columns=sorted(Sensors))

    # Make the prediction using the trained Random Forest model
    prediction = rfc.predict(input_df)[0]

    # Return the predicted room
    return prediction

