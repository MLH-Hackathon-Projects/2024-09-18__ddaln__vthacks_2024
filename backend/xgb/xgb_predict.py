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
    
    # load model
    model = xgb.XGBRegressor()
    model.load_model(CURR_MODEL_PATH)
    
    # dict to df
    test_df = pd.DataFrame(data_dict)
    
    # set columns
    expected_columns = ['age', 'num_people', 'mentioned_medical', 'mentioned_violence', 
                        'mentioned_fire', 'mentioned_vehicular', 'mentioned_mental_health',
                        'mentioned_natural_disasters', 'mentioned_environmental_hazards', 
                        'mentioned_suspicious_activity', 'mentioned_urgency']
    test_df = test_df.reindex(columns=expected_columns, fill_value=0)

    # severity score prediction based on model
    y_pred = model.predict(test_df)
    y_pred_value = float(y_pred[0])

    return round(y_pred_value, 3)

if __name__ == '__main__':
    # test case, should be ~8.5 +- 1.0
    data = {
        'age': [45],
        'num_people': [3],
        'mentioned_medical': [0],
        'mentioned_violence': [0],
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