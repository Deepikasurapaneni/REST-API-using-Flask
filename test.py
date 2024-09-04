import requests

BASE = "http://127.0.0.1:5000/"

# Sending a PATCH request with JSON data
r = requests.patch(BASE + "video/2", json={"views": 99})

# Print the raw response text
print("Response Status Code:", r.status_code)
print("Response Text:", r.text)

# Attempt to parse JSON if the response is expected to be in JSON format
try:
    response_json = r.json()
    print("Response JSON:", response_json)
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON from response")
