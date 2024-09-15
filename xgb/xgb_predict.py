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
        'age': [30],
        'num_people': [1],
        'mentioned_medical': [0],
        'mentioned_violence': [1],
        'mentioned_fire': [1],
        'mentioned_vehicular': [0],
        'mentioned_mental_health': [0],
        'mentioned_natural_disasters': [0],
        'mentioned_environmental_hazards': [0],
        'mentioned_suspicious_activity': [0],
        'mentioned_urgency': [1],
    }
    severity_score = predict_severity(CURR_MODEL_PATH, data)
    print(f"Prediction: {severity_score}")