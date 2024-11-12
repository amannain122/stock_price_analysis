## Stock Price Analysis
This project focuses on analyzing historical stock price data from Yahoo Finance to identify trends, patterns, and make price predictions of stock prices of the S&P 500 index, helping in future investment decisions.


## Project Overview
- **Goal**: To explore historical stock data, visualize trends, and predict future prices.
- **Data Source**: [Yahoo Finance](https://finance.yahoo.com)
- **Folder Structure**
```bash
stock_price_analysis/
├── data/                # Contains data files (raw data, cleaned data, etc.)
├── notebooks/           # Jupyter notebooks for analysis and modeling
├── models/              # Trained machine learning models (.pkl files)
├── src/                 # Flask app and related files (app.py)
├── requirements.txt     # Python dependencies for the project
├── Dockerfile           # Instructions to containerize the app
├── .dockerignore        # Files/folders to ignore during Docker build
├── .gitignore           # Git ignore rules (e.g., virtualenv, data, models)
└── README.md            # Project documentation
```
## Technologies Used
- **Python**: Programming language used for building the application.
- **Flask**: Web framework for creating the application.
- **yfinance**: For scraping S&P 500 historical data from Yahoo Finance.
- **Scikit-learn**: For building machine learning models.
- **Docker**: Containerization for deployment, making the app portable with FlaskAPI

## **Steps Taken**

### 1. **Data Collection and Preprocessing**
   - Scraped S&P 500 data from **Yahoo Finance** using **yfinance**.
   - **Processed the data**:
     - Filled missing values
     - Calculated **50-day Moving Average (50 MA)** 
     - Prepared the data for model training.
   - **Feature Engineering**:
     - Created new features like **daily returns** and **volatility** using a **30-day rolling window**.

### 2. **Exploratory Data Analysis (EDA)**
   - **Visualized the data**: Plotted price trends for **Open**, **Close**, **High**, and **Low** over time.
   - **Correlation Analysis**:
     - Analyzed the correlation between various features and the target variable (next day's opening price).
   - Added additional features:
     - **50-day moving average (50 MA)**
     - **Volatility** (30-day rolling window)

### 3. **Modeling**
   - Built multiple regression models to predict the next day’s opening price of the S&P 500:
     - **Linear Regression**
     - **Random Forest**
     - **Ridge Regression**
     - **Lasso Regression**
     - **XGBoost**
   - Trained the models using the prepared data.
   - Selected the best model based on **RMSE (Root Mean Squared Error)**.

### 4. **Model Evaluation**
   - **Cross-validation**: Evaluated all models using cross-validation to ensure they generalize well.
   - **Tested RMSE**: Calculated RMSE for both the **training** and **test** sets.

### 5. **Dockerization**
   - Containerized the Flask app and machine learning models using **Docker**.
   - Exposed the Flask service on **port 5000** to make it accessible for predictions.

### 6. **Deployment**
   - **Docker Hub**: Pushed the Docker image to Docker Hub for easy sharing and deployment.
   - Users can now **pull the Docker image** and run the model locally without needing to set up the environment manually.

---

## **How to Use**

### 1. **Run the Flask App**
   - Build the Docker image:
     ```bash
     docker build -t flask_app_1 .
     ```
   - Run the Docker container:
     ```bash
     docker run -p 5000:5000 flask_app_1
     ```

### 2. **Send Data for Prediction**
   - Use **curl** or **Postman** to send stock data to the `/predict` endpoint and receive predictions.

   Example **curl** request:
   ```bash
   curl -X POST -H "Content-Type: application/json" \
   -d "{\"Open\": 6008.86, \"High\": 6017.31, \"Low\": 5986.69, \"Close\": 6001.35, \"Adj Close\": 6001.35, \"50_MA\": 5735.44}" \
   http://127.0.0.1:5000/predict
