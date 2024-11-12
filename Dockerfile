# Step 1: Use Python 3.10 slim as the base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt from the parent directory into the container
COPY requirements.txt /app/requirements.txt

# Step 4: Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the models folder from the parent directory into the container
COPY models /app/models

# Step 6: Copy the src folder (which contains app.py) into the container
COPY src /app/src

# Step 7: Expose the Flask app on port 5000
EXPOSE 5000

# Step 8: Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]
