# Flask Metrics API

## Project Overview
A simple Flask application that reads simulated metrics from a JSON file and exposes them through a REST API endpoint.

## Technologies Used
- Python
- Flask
- JSON
- PythonAnywhere

## Project Files
- `flask_app.py` – Main Flask application.
- `sample_metrics.json` – Contains simulated metrics.
- `README.md` – Project documentation.

## Sample Metrics
The API returns:
- CPU: 22
- Memory: 68
- Requests: 1245

## API Details
- **Endpoint:** https://marryum32.pythonanywhere.com/metrics
- **HTTP Method:** GET
- **Response Format:** JSON

## How to Test
Run this command in your terminal:

```bash
curl https://marryum32.pythonanywhere.com/metrics
```

## Expected Response
```json
{
  "cpu": 22,
  "memory": 68,
  "requests": 1245
}
```

## Error Handling and Logging
- Uses try/except blocks to handle errors while reading the JSON file.
- Returns a JSON error message with HTTP status code 500 if an error occurs.
- Records incoming requests and errors in `app.log`.

## Deployment
The Flask API is deployed on PythonAnywhere and is publicly accessible through the API endpoint above.