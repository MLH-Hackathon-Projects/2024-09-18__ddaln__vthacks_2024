import pandas as pd
import xgboost as xgb

def predict_severity(data_dict: dict) -> float:
    """
    Predicts severity score using the provided XGBoost model and data dictionary.

    Parameters:
    - data_dict (dict): A dictionary containing the input features for prediction.

    Returns:
    - float: The predicted severity score rounded to 3 decimal places.
    """
    CURR_MODEL_PATH = 'backend/xgb/xgb_models/xgboost_model.json'
    # Load the model
    model = xgb.XGBRegressor()
    model.load_model(CURR_MODEL_PATH)
    
    # Convert dictionary to DataFrame
    test_df = pd.DataFrame(data_dict)
    
    # Predict
    y_pred = model.predict(test_df)
    
    # Ensure the prediction is a Python float
    y_pred_value = float(y_pred[0])
    
    # Return the prediction rounded to 3 decimal places
    return round(y_pred_value, 3)

if __name__ == '__main__':
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
        'mentioned_urgency': [1]
    }
    severity_score = predict_severity(data)
    print(f"Prediction: {severity_score}")
