## Part 9- Build the Payment Creation Endpoint

### Objective

Turn the basic FastAPI application into an actual payment API.

Implement:

`POST /v1/payments`

The endpoint will accept a payment request like:
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
and return a transaction response.

1. When Postman eventually sends:

POST `http://127.0.0.1:8000/v1/payments`

the flow will be:

```
Postman
   │
   │ POST /v1/payments
   │
   │ JSON payment data
   ▼
FastAPI
   │
   ├── Receive request
   │
   ├── Validate request
   │
   ├── Process payment
   │
   ├── Generate transaction ID
   │
   └── Return response
   ▼
Postman
```
Not adding authentication yet.

2. Why do we need request models?

payment JSON:
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

The API needs to know:

- Is `amount` present?
- Is it a number?
- Is `currency` present?
- Is `customer` present?
- Is `phone` present?
- Is `reference` present?

To avoid manual inspection of every JSON field.

FastAPI uses **Pydantic models** to handle this validation.
```
JSON request
     ↓
Pydantic model
     ↓
Valid?
 ┌───┴────┐
Yes       No
 ↓         ↓
Process   422
```

## Run the Program

`uvicorn main:app --reload`

### Terminal output

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [19772] using StatReload
INFO:     Started server process [12504]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Test the endpoint

Go to:

`http://127.0.0.1:8000/docs`

Check:

`POST /v1/payments`

Expand it and Click:

`Try it out`

FastAPI should give you a generated request body:

```
{
  "amount": 0,
  "currency": "string",
  "customer": {
    "phone": "string"
  },
  "reference": "string",
  "description": "string"
}
```
Replace it with:
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
Click **Execute**.