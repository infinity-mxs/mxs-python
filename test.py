import requests

body = {
    "title": "From Windows",
    "message": "TEST"
}

requests.post("http://192.168.100.20:5000/", json=body)