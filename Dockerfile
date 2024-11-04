# Stage 1: Build the application
FROM python:3.12-slim as builder

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose ports for development server and WebSocket
EXPOSE 8000

# Stage 2: Production Environment
FROM python:3.12-slim

# Set working directory to /app
WORKDIR /app

# Copy application code from builder
COPY --from=builder /app /app

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make migrations and migrate database
RUN python manage.py migrate

# Command to run on container launch
CMD ["daphne", "-p", "8000", "ryderbackend.asgi:application"]
