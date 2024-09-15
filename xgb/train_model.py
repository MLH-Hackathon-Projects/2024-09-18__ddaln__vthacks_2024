import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

MODEL = 'xgboost_model'

# Load dataset
df = pd.read_csv('incident_features.csv')
df_numeric = df.apply(pd.to_numeric, errors='coerce')
df_filled = df_numeric.fillna(0)
df_cleaned = df_filled.drop(columns=['severity'])

# Convert categorical variables
df['Location'] = df['Location'].astype('category').cat.codes
df['emergency_details'] = df['emergency_details'].astype('category').cat.codes

# Define feature set and target
X = df_cleaned[['Age','num_people','medical','violence','fire','vehicular','mental_health','natural_disasters','environmental_hazards','suspicious_activity','urgency']]
y = df['severity']
 
# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the XGBoost model
xg_reg = xgb.XGBRegressor(objective='reg:squarederror', colsample_bytree=0.5, learning_rate=0.1,
                          max_depth=3, alpha=0, n_estimators=50)
xg_reg.fit(X_train, y_train)

# Save the model
xg_reg.save_model(f'xgb/xgb_models/{MODEL}.json')
print(f"Model saved to xgb/xgb_models/{MODEL}.json")