import argparse
import requests
import sys
import flask
import json

app = flask.Flask(__name__)

# URL for API placeholder
API_URL = "https://sampleapis.com/api-list/beers"
# Default file for loading in the CLI
DEFAULT_OUTPUT_FILE = 'output.json'


def extract_from_api(url):
    """Extract data from the given API URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def extract_from_stdin():
    """Extract data from the standard input."""
    input_data = sys.stdin.read()
    return json.loads(input_data)


def transform(data):
    """Transform data as needed. This is a placeholder function."""
    # For example, you could filter or modify the data here
    return data


def load_to_file(data, output_file):
    """Load data to the given output file."""
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)


def load_to_stdout(data):
    json.dump(data, sys.stdout, indent=2)
    sys.stdout.write("\n")


def etl_process(stdin, url, output_file, stdout):
    """Run the ETL process using either stdin or URL for extraction."""
    if stdin:
        data = extract_from_stdin()
    else:
        data = extract_from_api(url)

    transformed_data = transform(data)
    if stdout:
        load_to_stdout(transformed_data)
    else:
        load_to_file(transformed_data, output_file)


@app.route('/etl', methods=['POST'])
def etl_endpoint():
    """HTTP endpoint for running the ETL process."""
    req_data = flask.request.json
    url = req_data.get('url', API_URL)
    output_file = req_data.get('output_file', DEFAULT_OUTPUT_FILE)

    data = extract_from_api(url)
    transformed_data = transform(data)

    return {"status": "success", "data": transformed_data}, 200


def main():
    parser = argparse.ArgumentParser(description='Run ETL process from CLI or server')
    parser.add_argument('--server', action='store_true', help='Run as a Flask server')
    parser.add_argument('--stdin', action='store_true', help='Extract data from stdin')
    parser.add_argument('--stdout', action='store_true', help='Extract data to stdout')
    parser.add_argument('--url', type=str, default=API_URL, help='URL to fetch data from for extraction')
    parser.add_argument('--port', type=str, default='5000', help='Server port')
    parser.add_argument('--output-file', type=str, default=DEFAULT_OUTPUT_FILE, help='Output file to load the data')

    args = parser.parse_args()

    if args.server:
        app.run(host='0.0.0.0', port=args.port)
    else:
        etl_process(args.stdin, args.url, args.output_file, args.stdout)


if __name__ == '__main__':
    main()