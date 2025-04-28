import requests

BASE = "http://127.0.0.1:5000/"

def test_put():
    print("Testing PUT method (Create Video)...")
    response = requests.put(BASE + "video/1", json={"name": "Video 1", "views": 100, "likes": 10})
    if response.status_code == 201:
        print("PUT Test Passed! Video created.")
    else:
        print("PUT Test Failed:", response.json())
    print(response.json())

def test_get():
    print("Testing GET method (Get Video)...")
    response = requests.get(BASE + "video/1")
    if response.status_code == 200:
        print("GET Test Passed! Video found.")
    else:
        print("GET Test Failed:", response.json())
    print(response.json())

def test_patch():
    print("Testing PATCH method (Update Video)...")
    response = requests.patch(BASE + "video/1", json={"views": 50, "likes": 43})
    if response.status_code == 200:
        print("PATCH Test Passed! Video updated.")
    else:
        print("PATCH Test Failed:", response.json())
    print(response.json())

def test_delete():
    print("Testing DELETE method (Delete Video)...")
    response = requests.delete(BASE + "video/1")
    if response.status_code == 204:
        print("DELETE Test Passed! Video deleted.")
    else:
        print("DELETE Test Failed:", response.json())
    print(response.status_code)

# Run all tests
def run_tests():
    test_put()
    test_get()
    test_patch()
    test_delete()

if __name__ == "__main__":
    run_tests()
