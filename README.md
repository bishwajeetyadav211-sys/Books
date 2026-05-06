# Address Book API

A robust RESTful API built with FastAPI to manage an address book. This application allows you to create, read, update, and delete addresses, along with a special feature to find addresses that are within a given distance from specific coordinates.

## Features

* **CRUD Operations**: Create, Read, Update, and Delete address entries.
* **Geospatial Search**: Find nearby addresses within a given distance (in kilometers) from a specified latitude and longitude using `geopy`.
* **Database Integration**: SQLite database with SQLAlchemy ORM.
* **Data Validation**: Request and response validation using Pydantic.
* **Interactive API Docs**: Built-in Swagger UI for easy testing and exploration of the API.

## Tech Stack

* **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
* **Database**: SQLite (default, easily configurable for others)
* **Data Validation**: [Pydantic](https://docs.pydantic.dev/)
* **Geospatial Calculations**: [Geopy](https://geopy.readthedocs.io/)
* **Server**: Uvicorn

## Project Structure

```
address-book/
│
├── app/
│   ├── main.py                 # Application entry point & FastAPI instance
│   ├── db/
│   │   └── database.py         # Database connection and session management
│   ├── models/
│   │   └── address.py          # SQLAlchemy models representing DB tables
│   ├── schemas/
│   │   └── address.py          # Pydantic schemas for data validation
│   └── routers/
│       ├── address_routes.py   # API endpoints routing
│       └── address_crud.py     # Database CRUD operations logic
│
├── test_api.py                 # Example script to test the API endpoints
└── requirements.txt            # Project dependencies (create if needed)
```

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

* Python 3.8 or higher installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd address-book
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   * **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   * **macOS / Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic geopy requests
   ```
   *(Note: `requests` is only needed if you want to run `test_api.py`)*

### Running the Application

1. **Start the FastAPI development server:**
   Ensure you are in the project root directory (`address-book/`) and your virtual environment is activated. Run:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API:**
   * The API will be available at: `http://127.0.0.1:8000`
   * **Interactive API Documentation (Swagger UI):** Open `http://127.0.0.1:8000/docs` in your browser. This is the easiest way to test the API endpoints.
   * **Alternative API Documentation (ReDoc):** Open `http://127.0.0.1:8000/redoc`

### Testing the API Programmatically

A test script `test_api.py` is included to demonstrate how to interact with the API using Python.

With the server running (in a separate terminal window), run the script:
```bash
python test_api.py
```
This will create addresses, fetch them, update one, retrieve addresses within a specific radius, and delete an address.

## API Endpoints Summary

* `POST /api/addresses/` - Create a new address
* `GET /api/addresses/` - Retrieve all addresses
* `GET /api/addresses/{address_id}` - Retrieve a specific address by its ID
* `PUT /api/addresses/{address_id}` - Update a specific address
* `DELETE /api/addresses/{address_id}` - Delete a specific address
* `GET /api/addresses/nearby` - Find addresses within a certain distance of given coordinates (query params: `lat`, `lon`, `distance`)
