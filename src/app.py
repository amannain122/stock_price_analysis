from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Check if the app is running inside a Docker container
if os.path.exists('/app/models'):
    # If inside Docker, use the Docker container path
    model_path = '/app/models/'
else:
    # If running locally, use the local path
    model_path = './models/'

# Load the trained models (update the path to match Docker's file structure)
rf_model = joblib.load(os.path.join(model_path, 'random_forest_model.pkl'))
lr_model = joblib.load(os.path.join(model_path, 'linear_regression_model.pkl'))
ridge_model = joblib.load(os.path.join(model_path, 'ridge_regression_model.pkl'))
lasso_model = joblib.load(os.path.join(model_path, 'lasso_regression_model.pkl'))
xgb_model = joblib.load(os.path.join(model_path, 'xgboost_model.pkl'))
stacked_model = joblib.load(os.path.join(model_path,'stacked_model.pkl'))


# Default route to test the server
@app.route('/')
def home():
    return "Welcome to the Flask app! Use the /predict endpoint for predictions."

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
    # stacked_pred = stacked_model.predict(features)

    # Create a response with predictions
    response = {
        'Random_Forest_Prediction': float(rf_pred[0]),
        'Linear_Regression_Prediction': float(lr_pred[0]),
        'Ridge_Regression_Prediction': float(ridge_pred[0]),
        'Lasso_Regression_Prediction': float(lasso_pred[0]),
        'XGBoost_Prediction': float(xgb_pred[0]),
        # 'Stacked_Model_Prediction': float(stacked_pred[0])
    }

    # Return the predictions as JSON response
    return jsonify(response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
