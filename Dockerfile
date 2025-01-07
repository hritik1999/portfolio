# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=5001
ENV WORKERS=4

# Copy only backend requirements and app files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE $PORT

# Command to run Gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT \
    --workers $WORKERS \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    app:app
