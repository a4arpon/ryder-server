# Ryder Backend - Taxi Management System

## Project Overview

This backend project, built with Django and Django Channels, provides API endpoints and WebSocket services for a Taxi
Management System. It supports real-time tracking, driver, and trip management with Redis caching to optimize data
retrieval.

## Features

- **Driver Management**: Create and retrieve driver profiles.
- **Trip Management**: Create and retrieve trip details, supporting live trip tracking.
- **Passenger Management**: Manage passengers and retrieve information.
- **Real-Time Trip Tracking**: WebSocket-based live tracking for real-time updates.
- **Caching**: Redis caching for trip data to enhance retrieval efficiency.

## Tech Stack

- **Framework**: Django, Django REST Framework, Django Channels
- **WebSocket**: Django Channels for WebSocket-based live tracking
- **Database**: PostgreSQL
- **Caching**: Redis
- **Dependencies**: `channels_redis`, `daphne`, `redis`

## Project Structure

```plaintext
backend/
├── apps/
│   └── api/
│       ├── consumers.py           # WebSocket consumers for real-time updates
│       ├── models.py              # Database models for Driver, Trip, Passenger
│       ├── serializers.py         # Serializers for API responses
│       ├── services/              # Business logic for drivers, trips, and passengers
│       │   ├── driver_services.py
│       │   ├── passenger_services.py
│       │   ├── realtime_services.py
│       │   └── trips_services.py
│       ├── urls.py                # API routes
│       └── views.py               # API views for CRUD operations
├── ryderbackend/
│   ├── asgi.py                    # ASGI config and WebSocket routing
│   ├── settings.py                # Project settings, including Redis and Channels config
│   ├── urls.py                    # Main URL routing
├── manage.py                      # Django management commands
└── requirements.txt               # Project dependencies
```

## Setup and Installation

### Prerequisites

- Python 3.12
- PostgreSQL
- Redis
- `virtualenv` or `venv` for environment management

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/a4arpon/ryder-server.git
   cd backend
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the `backend` directory:

   ```plaintext
   DB_NAME=""
   DB_USER=""
   DB_PASSWORD=""
   DB_HOST=""
   DB_PORT=""
   REDIS_PASSWORD=""
   SECRET_KEY=""
   ```

5. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create Superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**

   Choose one of the following commands:

    - **Daphne**:
      ```bash
      daphne -p 8000 ryderbackend.asgi:application
      ```
    - **Django Development Server**:
      ```bash
      python manage.py runserver
      ```

## API and WebSocket Endpoints

### API Endpoints

- **Driver Endpoints**
    - `POST /api/create-driver/`: Create a new driver.
    - `GET /api/get-drivers/`: Retrieve all drivers.
    - `GET /api/get-drivers/<driverID>/`: Retrieve details of a specific driver.

- **Passenger Endpoints**
    - `POST /api/create-passenger/`: Create a new passenger.
    - `GET /api/get-passengers/`: Retrieve all passengers.
    - `GET /api/get-passengers/<user_id>/`: Retrieve details of a specific passenger.

- **Trip Endpoints**
    - `POST /api/create-trip/`: Create a new trip.
    - `GET /api/get-trips/`: Retrieve all trips.
    - `GET /api/get-trips/<trip_id>/`: Retrieve details of a specific trip.

### WebSocket Endpoint

- **Real-Time Trip Updates**
    - Endpoint: `ws://127.0.0.1:8000/ws/trip_updates/`
    - Request Payload (JSON): `{ "trip-id": "tripID" }`
    - **Description**: Provides real-time location updates based on the trip ID provided.

## Redis Integration

The project uses Redis for caching trip data:

- **Caching**: Trip data is cached using keys in the format `trip-cache:<tripID>`.

## Services

- **Driver Services**: `driver_services.py` for driver-related logic.
- **Passenger Services**: `passenger_services.py` for passenger-related actions.
- **Trip Services**: `trips_services.py` to handle trip creation and retrieval.
- **Real-Time Services**: `realtime_services.py` for caching and retrieving real-time trip data from Redis.

## Deployment

Set environment variables for production in your server configuration. Ensure PostgreSQL and Redis servers are
configured and accessible.
