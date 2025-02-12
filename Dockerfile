# Use official Python 3.10-alpine image for smaller size
FROM python:3.10-alpine AS builder

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev

# Set working directory
WORKDIR /app

# Copy the requirements.txt first and install dependencies
COPY requirements.txt .

# Install Python dependencies (in one step to reduce layers)
RUN pip install --no-cache-dir -r requirements.txt

# Final image: Use a much smaller base image
FROM python:3.10-alpine

# Set working directory
WORKDIR /app

# Install runtime dependencies (only those required for your app)
RUN apk add --no-cache libffi

# Copy installed Python packages from the builder stage
COPY --from=builder /usr/local /usr/local

# Copy application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "run.py"]
