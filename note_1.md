# Exercise  — Build a Local Mock Payment API

## Objective

Build a small Fintech-style payment API running on my own computer.

```

                         Your Computer
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   Postman                                                │
│      │                                                  │
│      │ HTTP requests                                    │
│      ▼                                                  │
│   ┌───────────────────────────────┐                     │
│   │      Mock Payment API         │                     │
│   │                               │                     │
│   │  Authentication               │                     │
│   │  Request validation            │                     │
│   │  Payment processing            │                     │
│   │  Transaction IDs               │                     │
│   │  HTTP error handling           │                     │
│   └──────────────┬────────────────┘                     │
│                  │                                      │
│                  ▼                                      │
│            Mock data store                              │
│                                                         │
└─────────────────────────────────────────────────────────┘

```

Using Python + FastAPI.

Why FastAPI?

- It's relatively easy to understand.
- It exposes real HTTP endpoints.
- It gives us proper HTTP status codes.
- It automatically provides API documentation.
- It's widely useful knowledge for someone working with APIs.
- You can interact with it directly from Postman.

## Part 1

Initial API will have two endpoints.

### 1. Create payment
`POST /v1/payments`

Example request:

```
{
  "amount": 2500,

  "currency": "KES",

  "customer": {

    "phone": "254712345678"
  },
  "reference": "ACME-20260914-001",
  "description": "Order payment"
}
```

Successful response:
```
{
  "transaction_id": "txn_...",
  "status": "successful",
  "amount": 2500,
  "currency": "KES",
  "reference": "ACME-20260914-001"
}
```

### 2. Retrieve payment
`
GET /v1/payments/{transaction_id}`

For example:

`
GET /v1/payments/txn_8f31a92c`

## Part 2 — Authentication

Simulate a Bearer-token authentication system.

The client will send:

`
Authorization: Bearer test_token_123`

The API will check the token.

For example:

```
Correct token
     ↓
Request accepted
     ↓
201 Created
```
but:
```
Missing token
     ↓
401 Unauthorized
```
and:
``` 
Wrong token
     ↓
401 Unauthorized
```

## Part 3 — Project structure
```
local_payment_api/
│
├── main.py
├── requirements.txt
├── notes.md
└── README.md
```

## Part 4- Create a virtual environment

Run:

`python -m venv .venv`

Activate it:

`.venv\Scripts\Activate.ps1`

### Why are we doing this?

Imagine you have:

```
Project A → FastAPI version X
Project B → FastAPI version Y
```

Installing everything globally can cause dependency conflicts.

A virtual environment gives each project its own Python dependencies.

## Part 5- Install FastAPI and Uvicorn

Run:

`pip install fastapi uvicorn`

Verify:

`pip show fastapi`

and:

`pip show uvicorn`

## Part 6- Start the API

Run:

`uvicorn main:app --reload`

Sample output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started reloader process [10604] using StatReload
INFO:     Started server process [7152]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Keep this PowerShell window running.

The API is now listening on:

`http://127.0.0.1:8000`

## Part 7- Test it manually

Open the browser and go to:

http://127.0.0.1:8000/

Output:

```
{
    "service": "Mock Payment API",
    "status": "running"
}
```

That means:

```
Browser
   │
   │ GET /
   ▼
127.0.0.1:8000
   │
   ▼
FastAPI
   │
   ▼
root()
   │
   ▼
JSON response

```
Successfully Created and accessed the local API.

## Part 8- Useful FastAPI feature
Open:

`http://127.0.0.1:8000/docs`

An interactive API documentation interface can be observed.

FastAPI automatically generated it.

Check:

`GET /`

Expand it and execute the endpoint from the browser.

This is called OpenAPI/Swagger documentation.


