from datetime import datetime

from httpx import Client, Request, Response


def log_request(request: Request):
    request.extensions['start_time'] = datetime.now()
    print(f"REQUEST: {request.method}")


def log_response(response: Response):
    duration = datetime.now() - response.request.extensions['start_time']
    print(f"RESPONSE:{response.status_code}, {duration}")


client = Client(
    base_url="http://127.0.0.1:8003",
    event_hooks={"request": [log_request], "response": [log_response]}
)
response = client.get("/api/v1/users/ef389671-20e2-403b-85e6-63941bb3d026")

print(response)
