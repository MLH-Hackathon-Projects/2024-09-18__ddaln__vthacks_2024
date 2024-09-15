import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# turn tuning on/off
TUNING = False
MODEL = 'xgboost_model'

# read in csv data
df = pd.read_csv('../incident_features.csv')
df_numeric = df.apply(pd.to_numeric, errors='coerce')
df_filled = df_numeric.fillna(0)
df_cleaned = df_filled.drop(columns=['severity'])

# convert cat vars
df['location'] = df['location'].astype('category').cat.codes
df['emergency_details'] = df['emergency_details'].astype('category').cat.codes

# clean feature set
X = df_cleaned[['age','num_people','mentioned_medical','mentioned_violence','mentioned_fire','mentioned_vehicular','mentioned_mental_health','mentioned_natural_disasters','mentioned_environmental_hazards','mentioned_suspicious_activity','mentioned_urgency']]
y = df['severity']

# set training/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initialize model
model = xgb.XGBRegressor()
model.load_model(f'xgb/xgb_models/{MODEL}.json')

# get severity prediction
y_pred = model.predict(X_test)

# check accuracy
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Y Prediction: {y_pred}")

# hyperparameter tuning
if TUNING:
    # parameters to compare/check
    param_grid = {
    'max_depth': [3, 4, 5, 6, 7, 8],
    'learning_rate': [0.01, 0.05, 0.1, 0.15, 0.2],
    'n_estimators': [50, 100, 150, 200, 250],
    'alpha': [0, 1, 10, 20, 30],
    'colsample_bytree': [0.3, 0.5, 0.7]
    }

    # initialize
    xg_reg = xgb.XGBRegressor(objective='reg:squarederror')

    # grid search
    grid_search = GridSearchCV(estimator=xg_reg, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)

    # find best parameters
    best_params = grid_search.best_params_
    best_model = grid_search.best_estimator_

    print(f"Best parameters: {best_params}")

    # TODO evaluate best model
    y_pred = best_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")