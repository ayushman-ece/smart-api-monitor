
import requests
import time

def check_api(url):
    start_time = time.time()

    try:
        response = requests.get(url, timeout=10)

        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)

        print("Status Code:", response.status_code)
        print("Response Time:", response_time, "ms")
        print("API Status:", "Online" if response.ok else "Error")

        return response

    except requests.exceptions.RequestException as error:
        print("API Connection Failed:", error)
        return None

def analyze_json(response):
    if response is None:
        print("No response available to analyze.")
        return

    try:
        data = response.json()

        print("\n===== JSON ANALYSIS =====")

        if isinstance(data, list):
            print("Data Type: List")
            print("Total Records:", len(data))

            if data and isinstance(data[0], dict):
                print("Available Fields:", list(data[0].keys()))

            print("\nFirst Record:")
            print(data[0] if data else "No records found")

        elif isinstance(data, dict):
            print("Data Type: Dictionary")
            print("Total Keys:", len(data))
            print("Available Keys:", list(data.keys()))

        else:
            print("Data Type:", type(data).__name__)
            print("Data:", data)

    except ValueError:
        print("Error: API did not return valid JSON.")
