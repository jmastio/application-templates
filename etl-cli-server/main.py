import argparse
import requests
import sys
import flask
import json
import logging
from flask import jsonify

app = flask.Flask(__name__)

# Configuration
API_URL = "https://api.sampleapis.com/beers/ale"
DEFAULT_OUTPUT_FILE = 'output.json'
LOG_FILE = 'app.log'

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_from_api(url):
    """Extract data from the given API URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from API URL {url}: {e}")
        raise


def extract_from_stdin():
    """Extract data from the standard input."""
    try:
        input_data = sys.stdin.read()
        return json.loads(input_data)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON data from stdin: {e}")
        raise


def transform(data):
    """Transform data as needed. This is a placeholder function."""
    # For example, you could filter or modify the data here
    return data


def load_to_file(data, output_file):
    """Load data to the given output file."""
    try:
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        logging.info(f"Data successfully loaded to {output_file}")
    except IOError as e:
        logging.error(f"Error writing data to file {output_file}: {e}")
        raise


def load_to_stdout(data):
    """Load data to the standard output."""
    try:
        json.dump(data, sys.stdout, indent=2)
        sys.stdout.write("\n")
        logging.info("Data successfully written to stdout")
    except Exception as e:
        logging.error(f"Error writing data to stdout: {e}")
        raise


def etl_process(stdin, url, output_file, stdout):
    """Run the ETL process using either stdin or URL for extraction."""
    try:
        if stdin:
            data = extract_from_stdin()
        else:
            data = extract_from_api(url)

        transformed_data = transform(data)

        if stdout:
            load_to_stdout(transformed_data)
        else:
            load_to_file(transformed_data, output_file)
    except Exception as e:
        logging.error(f"ETL process failed: {e}")
        raise


@app.route('/etl', methods=['POST'])
def etl_endpoint():
    """HTTP endpoint for running the ETL process."""
    try:
        req_data = flask.request.json
        url = req_data.get('url', API_URL)

        data = extract_from_api(url)
        transformed_data = transform(data)

        # load is just returning data
        return jsonify({"status": "success", "data": transformed_data}), 200
    except Exception as e:
        logging.error(f"Failed to process ETL request: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


def main():
    parser = argparse.ArgumentParser(description='Run ETL process from CLI or server.')
    parser.add_argument('--server', action='store_true', help='Run as a Flask server.')
    parser.add_argument('--stdin', action='store_true', help='Extract data from stdin.')
    parser.add_argument('--stdout', action='store_true', help='Extract data to stdout.')
    parser.add_argument('--url', type=str, default=API_URL, help='URL to fetch data from for extraction.')
    parser.add_argument('--port', type=int, default=5000, help='Server port.')
    parser.add_argument('--output-file', type=str, default=DEFAULT_OUTPUT_FILE, help='Output file to load the data.')

    args = parser.parse_args()

    logging.info("Starting ETL process...")

    if args.server:
        logging.info(f"Starting server on port {args.port}")
        app.run(host='0.0.0.0', port=args.port)
    else:
        try:
            etl_process(args.stdin, args.url, args.output_file, args.stdout)
        except Exception as e:
            logging.error(f"ETL process encountered an error: {e}")
            sys.exit(1)


if __name__ == '__main__':
    main()