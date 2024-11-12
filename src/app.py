from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained models 
rf_model = joblib.load('models/random_forest_model.pkl')
lr_model = joblib.load('models/linear_regression_model.pkl')
ridge_model = joblib.load('models/ridge_regression_model.pkl')
lasso_model = joblib.load('models/lasso_regression_model.pkl')
xgb_model = joblib.load('models/xgboost_model.pkl')
stacked_model = joblib.load('models/stacked_model.pkl')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract features from the input data
    features = np.array([data['Open'], data['High'], data['Low'], data['Close'], data['Adj Close'], data['50_MA']]).reshape(1, -1)

    # Get predictions from each model
    rf_pred = rf_model.predict(features)
    lr_pred = lr_model.predict(features)
    ridge_pred = ridge_model.predict(features)
    lasso_pred = lasso_model.predict(features)
    xgb_pred = xgb_model.predict(features)
    stacked_pred = stacked_model.predict(features)

    # Create a response with predictions
    response = {
        'Random_Forest_Prediction': rf_pred[0],
        'Linear_Regression_Prediction': lr_pred[0],
        'Ridge_Regression_Prediction': ridge_pred[0],
        'Lasso_Regression_Prediction': lasso_pred[0],
        'XGBoost_Prediction': xgb_pred[0],
        'Stacked_Model_Prediction': stacked_pred[0]
    }

    # Return the predictions as JSON response
    return jsonify(response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
