import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

MODEL = 'xgboost_model'

# read in csv data
df = pd.read_csv('backend/incident_features.csv')
df_numeric = df.apply(pd.to_numeric, errors='coerce')
df_filled = df_numeric.fillna(0)
df_cleaned = df_filled.drop(columns=['severity'])

# convert cat vars
df['location'] = df['location'].astype('category').cat.codes
df['emergency_details'] = df['emergency_details'].astype('category').cat.codes

# df for feature set
X = df_cleaned[['age','num_people','mentioned_medical','mentioned_violence','mentioned_fire','mentioned_vehicular','mentioned_mental_health','mentioned_natural_disasters','mentioned_environmental_hazards','mentioned_suspicious_activity','mentioned_urgency']]
y = df['severity']
 
# set training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initialize regressor
xg_reg = xgb.XGBRegressor(objective='reg:squarederror', colsample_bytree=0.5, learning_rate=0.1,
                          max_depth=3, alpha=0, n_estimators=50)
xg_reg.fit(X_train, y_train)

# save trained model
xg_reg.save_model(f'backend/xgb/xgb_models/{MODEL}.json')
print(f"Model saved to backend/xgb/xgb_models/{MODEL}.json")