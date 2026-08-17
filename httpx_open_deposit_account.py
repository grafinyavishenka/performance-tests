import time
import httpx

BASE_URL = "http://127.0.0.1:8003"

create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post(f"{BASE_URL}/api/v1/users", json=create_user_payload)
account_payload = {"userId": create_user_response.json()["user"]["id"]}
account_response = httpx.post(
    f"{BASE_URL}/api/v1/accounts/open-deposit-account", json=account_payload
)

print(account_response.text)
print(account_response.status_code)
