# ETL Process Application

## Overview
This application runs an ETL (Extract, Transform, Load) process either from the command line or as a Flask-based HTTP server.

## Requirements
- Python 3.x
- Flask
- Requests

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/etl-process.git
   cd etl-process
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### CLI Mode

Run the ETL process from the command line with various options:

```bash
python etl_process.py [options]
```

Options:
- `--server`: Run as a Flask server.
- `--stdin`: Extract data from stdin.
- `--stdout`: Extract data to stdout.
- `--url URL`: URL to fetch data from (default: `https://sampleapis.com/api-list/beers`).
- `--port PORT`: Server port (default: `5000`).
- `--output-file FILE`: Output file (default: `output.json`).

### Server Mode

Run as a Flask server:

```bash
python etl_process.py --server
```
This starts the server on port 5000 by default. Change with the `--port` option.

### API Endpoint

- **Endpoint**: `/etl`
- **Method**: POST
- **Content-Type**: application/json
- **Payload example**:
  ```json
  {
    "url": "https://sampleapis.com/api-list/beers",
    "output_file": "output.json"
  }
  ```
- **Response example**:
  ```json
  {
    "status": "success",
    "data": [ ... ]
  }
  ```

### Docker

#### Build the Docker Image

```bash
docker build -t etl-process .
```

#### Run ETL Server

```bash
docker run -p 5000:5000 etl-process
```
The server starts on port 5000 at `http://localhost:5000/etl`.

#### Run ETL from Command Line

```bash
docker run --rm -v $(pwd):/app etl-process python etl_process.py [options]
```

Example to output to stdout:
```bash
docker run --rm -v $(pwd):/app etl-process python etl_process.py --stdout
```

#### Run ETL from a JSON File

```bash
cat data.json | docker run --rm -i etl-process python etl_process.py --stdin --stdout
```

## Examples

- **Run ETL process and output to stdout**:
  ```bash
  python etl_process.py --stdout
  ```

- **Run ETL process from stdin**:
  ```bash
  cat data.json | python etl_process.py --stdin --stdout
  ```

- **Run ETL server**:
  ```bash
  python etl_process.py --server
  ```

By default, the server starts at `http://0.0.0.0:5000`.

## License
This project is licensed under the MIT License.
