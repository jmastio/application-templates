# ETL Process Application

## Overview
This application allows you to run an ETL (Extract, Transform, Load) process either from the command line or as a Flask-based HTTP server. 

- **Extraction** can be done from a REST API or from the standard input.
- **Transformation** is currently a placeholder function but can be customized as needed.
- **Load** the transformed data into a file or print to standard output.

## Requirements
- Python 3.x
- Flask
- Requests

## Installation
Clone the repository and install the required packages:
```bash
git clone https://github.com/your-repo/etl-process.git
cd etl-process
pip install -r requirements.txt
```

## Usage

### CLI Mode
You can run the ETL process from the command line with various options:

```bash
python etl_process.py [options]
```

Options:
- `--server`: Run as a Flask server.
- `--stdin`: Extract data from stdin.
- `--stdout`: Extract data to stdout.
- `--url URL`: URL to fetch data from for extraction (default: `https://sampleapis.com/api-list/beers`).
- `--port PORT`: Server port (default: `5000`).
- `--output-file FILE`: Output file to load the data (default: `output.json`).

### Server Mode
To run the ETL process as a Flask server:

```bash
python etl_process.py --server
```

This will start a server on port 5000 by default, which you can change using the `--port` option.

### API Endpoint
The server provides an endpoint `/etl` that accepts POST requests with a JSON payload to run the ETL process.

```http
POST /etl
Content-Type: application/json

{
    "url": "https://sampleapis.com/api-list/beers",
    "output_file": "output.json"
}
```

Response:

```json
{
    "status": "success",
    "data": [ ... ]  // transformed data
}
```

## Examples

### Run ETL process and output to stdout:
```bash
python etl_process.py --stdout
```

### Run ETL process from stdin:
```bash
cat data.json | python etl_process.py --stdin --stdout
```

### Run ETL server:
```bash
python etl_process.py --server
```
By default, this will start the server at `http://0.0.0.0:5000`.

## License
This project is licensed under the MIT License.