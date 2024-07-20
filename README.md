# Application Templates

Welcome to the **Application Templates** repository! This collection is designed to offer ready-to-use application archetypes for various use cases, allowing you to jumpstart your projects with well-structured templates.

## Table of Contents

- [etl-cli-server](#etl-cli-server)
    - [Installation](#installation)
    - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

### etl-cli-server

`etl-cli-server` is a versatile application template that provides a combination of a Command-Line Interface (CLI) and a Flask server. This template offers a rapid development framework suitable for building Extract, Transform, Load (ETL) processes. Whether you prefer to use stdin/out or develop a full-fledged Flask application, `etl-cli-server` has got you covered.

---

### Installation

To set up the `etl-cli-server` template locally:

1. Clone the repository:
    ```shell
    git clone https://github.com/your-username/application-templates.git
    ```
2. Navigate to the `etl-cli-server` directory:
    ```shell
    cd application-templates/etl-cli-server
    ```
3. Install the required dependencies:
    ```shell
    pip install -r requirements.txt
    ```

---

### Usage

Here's a quick guide on how to use the `etl-cli-server` template:

#### CLI Mode

1. Run the ETL process via the command line:
    ```shell
    python etl_cli.py <input_data>
    ```

#### Flask Server Mode

1. Start the Flask server:
    ```shell
    python etl_server.py
    ```
2. Access the server on your browser at `http://localhost:5000`.

---

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request. Here are the steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
