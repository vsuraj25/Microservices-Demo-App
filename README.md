# Microservices Demo Application

A simple demonstration of microservices architecture with CRUD operations and API integrations.

## Architecture

- **React Frontend** - User interface
- **Django Admin** - Custom admin panel (Port 8000)
- **Flask API** - Main API service (Port 8001)
- **RabbitMQ** - Message broker for service communication
- **Docker** - Containerization

## Project Structure

```
├── admin/              # Django admin service
├── flask-app/          # Flask API service
├── react-app/          # React frontend
└── docker-compose.yml  # Container orchestration
```

## Features

- CRUD operations on products
- Microservices communication via RabbitMQ
- REST APIs
- Docker containerization
- Admin interface

## Technologies Used

- **Frontend**: React, TypeScript
- **Backend**: Django, Flask, Python
- **Message Queue**: RabbitMQ
- **Database**: MySQL
- **Containerization**: Docker

## Setup and Installation

### Prerequisites
- Docker
- Docker Compose

### Run the Application

1. Clone the repository
```bash
git clone <repo-url>
cd microservices-demo
```

2. Start all services
```bash
docker-compose up --build
```

3. Access the services:
   - Django Admin: http://localhost:8000/admin/
   - Flask API: http://localhost:8001/api/
   - React App: http://localhost:3000/
   - RabbitMQ Management: http://localhost:15672/ (guest/guest)

## API Endpoints

### Flask API (Port 8001)
- `GET /api/products/` - Get all products
- `POST /api/products/` - Create product
- `GET /api/products/{id}/` - Get product by ID
- `PUT /api/products/{id}/` - Update product
- `DELETE /api/products/{id}/` - Delete product

### Django Admin (Port 8000)
- `/admin/` - Admin panel
- `/api/` - Admin API endpoints

## Usage Example

Create a product:
```bash
curl -X POST http://localhost:8001/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Product", "price": 25.99}'
```

Get all products:
```bash
curl http://localhost:8001/api/products/
```

## Development

Run individual services:
```bash
# Django admin
docker-compose up admin

# Flask API
docker-compose up flask-app

# React frontend
docker-compose up react-app
```

## RabbitMQ Integration

Services communicate through RabbitMQ message queues for:
- Product creation events
- Product update events  
- Product deletion events
