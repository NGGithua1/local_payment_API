## Part 10: Add Bearer Token Authentication

Anyone who knows:

`POST http://127.0.0.1:8000/v1/payments`

Can submit a payment. That's unrealistic for a payment API.

Change the API so that a merchant must provide a valid **Bearer token**.

The flow becomes:
```
Merchant / Postman
       │
       │ POST /v1/payments
       │ Authorization: Bearer <token>
       ▼
┌─────────────────────┐
│   Mock Payment API  │
│                     │
│  1. Check token     │
│  2. Validate body   │
│  3. Process payment │
└─────────────────────┘
       │
       ▼
    Response
```
### 1. Test credentials

For the local simulation, use:

`test_token_123`

The client must send:

`Authorization: Bearer test_token_123`

**Valid token**

`Authorization: Bearer test_token_123`

→ payment processing continues.

**Invalid token**

`Authorization: Bearer wrong_token`

→ output

`401 Unauthorized.`

**No token**

`No Authorization header.`

→ output

`401 Unauthorized.`