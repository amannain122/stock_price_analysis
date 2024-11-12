# Step 1: Use a specific Python version as a base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy requirements.txt from the parent directory to the container's working directory
COPY requirements.txt /app/requirements.txt

# Step 4: Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the models folder from the parent directory into the container's /app/models
COPY models /app/models

# Step 6: Copy the src folder (which contains your app.py) to the container
COPY src /app/src

# Step 7: Expose port 5000 to allow access to the Flask app
EXPOSE 5000

# Step 8: Set environment variable to disable buffering of logs
ENV PYTHONUNBUFFERED=1

# Step 9: Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]
