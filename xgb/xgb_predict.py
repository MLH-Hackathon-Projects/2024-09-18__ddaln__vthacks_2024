import pandas as pd
import xgboost as xgb

def predict_severity(model_path: str, data_dict: dict) -> float:
    """
    Predicts severity score using the provided XGBoost model and data dictionary.

    Parameters:
    - model_path (str): The path to the XGBoost model file.
    - data_dict (dict): A dictionary containing the input features for prediction.

    Returns:
    - float: The predicted severity score.
    """
    # Load the model
    model = xgb.XGBRegressor()
    model.load_model(model_path)
    
    # Convert dictionary to DataFrame
    test_df = pd.DataFrame(data_dict)
    
    # Predict
    y_pred = model.predict(test_df)
    
    # Return the prediction
    return y_pred[0]

if __name__ == '__main__':
    # Example usage
    CURR_MODEL_PATH = 'xgb/xgb_models/xgboost_model.json'
    data = {
        'Age': [50],
        'num_people': [3],
        'medical': [0],
        'violence': [0],
        'fire': [1],
        'vehicular': [0],
        'mental_health': [0],
        'natural_disasters': [0],
        'environmental_hazards': [0],
        'suspicious_activity': [0],
        'urgency': [1],
    }
    severity_score = predict_severity(CURR_MODEL_PATH, data)
    print(f"Prediction: {severity_score}")