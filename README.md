
# Fitness Booking API

A simple backend API for booking fitness classes, built with **FastAPI** and **SQLite**. This project demonstrates timezone-aware class scheduling, booking management, and validation using a lightweight Python stack.

---

## Features

- **FastAPI backend** with automatic OpenAPI docs
- SQLite database (file-based, no server setup)
- Timezone-aware class scheduling (stored in IST, converted on request)
- Class booking with slot availability checks (prevents overbooking)
- Retrieve bookings by client email
- Input validation and error handling
- Modular and clean Python code structure

---

## Technologies Used

- Python 3.13+
- FastAPI
- SQLAlchemy ORM
- SQLite
- Pydantic for data validation
- Uvicorn ASGI server

---

## Getting Started

### Prerequisites

- Python 3.13 or later installed
- Git (optional, for cloning)
- cURL or Postman for API testing

### Setup Instructions

1. **Clone the repo** (or download the source):
   ```bash
   git clone https://github.com/yourusername/fitness-booking-api.git
   cd fitness-booking-api
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**:
   ```bash
   uvicorn main:app --reload --port 8002
   ```

5. **Access API docs** at:
   ```
   http://127.0.0.1:8002/docs
   ```

---

## API Endpoints

### 1. Get all classes

- **GET** `/classes?tz=Your/Timezone`
- Returns all fitness classes with date/time converted to the requested timezone (default: `Asia/Kolkata`).

**Example:**
```bash
curl -X GET "http://127.0.0.1:8002/classes?tz=America/New_York" -H "accept: application/json"
```

---

### 2. Book a class

- **POST** `/book`
- Request body: JSON with booking info
- Books a slot if available; returns error if full or invalid.

**Sample request body:**
```json
{
  "class_id": 1,
  "client_name": "John Doe",
  "client_email": "john@example.com"
}
```

**Example cURL:**
```bash
curl -X POST "http://127.0.0.1:8002/book" \
     -H "Content-Type: application/json" \
     -d '{"class_id":1,"client_name":"John Doe","client_email":"john@example.com"}'
```

---

### 3. Get bookings by email

- **GET** `/bookings?email=client@example.com`
- Returns all bookings made by the specified email.

**Example cURL:**
```bash
curl -X GET "http://127.0.0.1:8002/bookings?email=john@example.com" -H "accept: application/json"
```

---

## Timezone Handling

- Classes are stored internally in IST (Asia/Kolkata).
- The `/classes` endpoint converts class times to the requested timezone using the `tz` query parameter.
- You can pass any valid IANA timezone string (e.g., `UTC`, `America/New_York`, `Europe/London`).

---

## Error Handling

- Booking a full or non-existent class returns HTTP 400 with an error message.
- Input validation errors return HTTP 422.
- Missing required fields are automatically flagged by Pydantic.

---

## Project Structure

\`\`\`
fitness-booking-api/
├── main.py           # FastAPI app & routes
├── models.py         # Pydantic models for requests/responses
├── models_db.py      # SQLAlchemy ORM models
├── crud.py           # Database CRUD operations
├── database.py       # DB connection setup
├── seed_data.py      # Initial data population
├── utils.py          # Utility functions (timezone conversions)
├── requirements.txt  # Python dependencies
└── README.md         # This documentation
\`\`\`

---

## Testing with Postman

1. Start your FastAPI server.
2. Import API endpoints manually or use `/docs` OpenAPI spec.
3. Send requests using the above cURL examples converted to Postman.
4. Change timezone, book classes, and fetch bookings as needed.

---