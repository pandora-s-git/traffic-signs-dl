import requests

url = "https://chat.mistral.ai/chat"

headers = {
    "Content-Type": "application/json",
}

data = {
    "messages": [{"role": "user", "content": "hello"}],
    "mode": "retry",
    "model": "mistral-large",
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    print(response.content)
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response:")
    print(response.text)
