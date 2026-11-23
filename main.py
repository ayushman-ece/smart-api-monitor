
import csv
import time

from api_monitor import check_api, analyze_json

urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/invalid"
]

results = []

print("=" * 55)
print("             SMART API RESPONSE MONITOR")
print("=" * 55)

for url in urls:
    print("\nChecking:", url)

    start_time = time.perf_counter()
    response = check_api(url)
    elapsed_time = round(
        (time.perf_counter() - start_time) * 1000, 2
    )

    if response is not None:
        analyze_json(response)

        status_code = response.status_code
        api_status = "Online" if response.ok else "Error"
    else:
        status_code = "Connection Failed"
        api_status = "Offline"

    results.append({
        "URL": url,
        "Status Code": status_code,
        "API Status": api_status,
        "Response Time (ms)": elapsed_time
    })

    print("-" * 55)

# Generate CSV report
with open("api_report.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "URL",
        "Status Code",
        "API Status",
        "Response Time (ms)"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("\n========== FINAL SUMMARY ==========")
print("Total APIs Checked:", len(results))
print("Online:", sum(r["API Status"] == "Online" for r in results))
print("Errors:", sum(r["API Status"] == "Error" for r in results))
print("Offline:", sum(r["API Status"] == "Offline" for r in results))
print("\nReport saved as: api_report.csv")
