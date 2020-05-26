# User profile endpoint

# Request
```http request
GET /api/v1/user/profile/
```

# Response
When logged in:

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "username": "admin",
    "first_name": "Jacek",
    "last_name": "Palczewski",
    "email": "admin@admin.pl"
}
```

When not logged in:

```http request
HTTP 403 Forbidden
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "Authentication credentials were not provided."
}
```