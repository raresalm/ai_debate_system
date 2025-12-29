# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy our files into the container
COPY . .

# Install the libraries from our requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Open port 8000 for the website
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]