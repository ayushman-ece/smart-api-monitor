# 📡 Smart API Response Monitor & JSON Analyzer

## 📌 Project Overview

The **Smart API Response Monitor & JSON Analyzer** is a Python-based tool that monitors multiple API endpoints, checks their HTTP response status, measures response time, analyzes JSON responses, and generates a CSV monitoring report.

It helps developers understand API availability, response behavior, and basic performance through a simple command-line application.

## 🎯 Objectives

- Monitor multiple API endpoints.
- Check HTTP response status codes.
- Measure API response time.
- Analyze JSON response structures.
- Handle connection errors and invalid JSON responses.
- Generate structured CSV monitoring reports.

## ⚙️ Features

- **API Health Checking:** Sends GET requests to API endpoints.
- **HTTP Status Monitoring:** Identifies successful and unsuccessful responses.
- **Response Time Measurement:** Measures the time taken by API requests.
- **JSON Analyzer:** Identifies response types, record counts, and available fields.
- **Multiple API Monitoring:** Checks several endpoints in one execution.
- **Error Handling:** Handles connection failures and invalid JSON responses.
- **CSV Report Generation:** Saves monitoring results in a structured CSV file.

## 🧠 Workflow

1. Define a list of API endpoints.
2. Send GET requests using the Requests library.
3. Capture HTTP status codes and response times.
4. Check whether each API is online or returning an error.
5. Parse and analyze JSON responses.
6. Store monitoring results in a list of dictionaries.
7. Export the results into a CSV report.
8. Display a final monitoring summary.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Requests | Sending HTTP GET requests |
| JSON | Parsing API responses |
| CSV | Generating monitoring reports |
| Time | Measuring response duration |

## 📊 Report Information

The generated `api_report.csv` contains:

- API URL
- HTTP Status Code
- API Status
- Response Time (ms)

The project uses JSONPlaceholder endpoints for demonstration and testing.

## 🔍 Technical Concepts

### 1. API Requests
Uses `requests.get()` to retrieve information from API endpoints.

### 2. HTTP Status Codes
- 200: Successful response.
- 404: Requested resource not found.
- Other unsuccessful responses are identified as errors.

### 3. JSON Analysis
Uses `response.json()` to convert JSON response data into Python objects and inspect lists and dictionaries.

### 4. Performance Measurement
Uses `time.perf_counter()` to measure elapsed request time.

### 5. Exception Handling
Uses `try-except` to handle request failures and invalid JSON responses.

### 6. CSV Export
Uses `csv.DictWriter()` to generate a structured monitoring report.

## 📁 Project Structure

```text
smart-api-monitor/
│
├── main.py
├── api_monitor.py
├── requirements.txt
├── .gitignore
└── api_report.csv       # Generated after execution
```

## 🚀 Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/ayushman-ece/smart-api-monitor.git
```

### 2. Navigate into the project

```bash
cd smart-api-monitor
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

### 5. View the generated report

After execution, open `api_report.csv` in a spreadsheet application or text editor.

## 📚 Key Concepts Learned

- REST API fundamentals
- HTTP GET requests
- HTTP status codes
- JSON parsing and Python data structures
- Python functions and loops
- Exception handling
- API response-time measurement
- CSV file handling
- Dictionary-based data processing

## ⚠️ Limitations

- The project performs checks only when manually executed.
- It does not continuously monitor APIs in the background.
- The current implementation uses predefined API endpoints.
- Response times can vary depending on network conditions.
- It does not include authentication handling or advanced API security checks.

## 🔮 Future Improvements

- Add continuous API monitoring.
- Support user-defined API endpoints.
- Generate graphical performance reports.
- Add response-time thresholds and alerts.
- Store historical monitoring results.
- Introduce scheduled monitoring.

## 👨‍💻 Author

**Ayushman Tiwari**

B.Tech – Electronics and Communication Engineering

GitHub: https://github.com/ayushman-ece

---

⭐ If you find this project useful, consider giving it a star!