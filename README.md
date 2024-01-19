# ThousandEyes Telescope CLI

![Telescope CLI](telescope.jpeg)

This Python script is a Command Line Interface (CLI) application designed to interact with the ThousandEyes API, using a syntax similar to Cisco devices. The application gives users the ability to execute various "show" commands, similar to a network operating system command-line interface (CLI).

The CLI retrieves and formats data from the ThousandEyes API, displaying it in multiple output formats including YAML, CSV, JSON, and human-readable format. This variety of output formats enables users to easily analyze and manipulate the data according to their needs.

One of the key features of this CLI is that it requires the ThousandEyes API Bearer Token to be entered only once. After initial input, the application retains the token for the duration of the session, allowing for continuous interaction with the API without the need to repeatedly enter the token.

The CLI offers two primary methods for data output. The first is to print the API response data directly to the terminal window. Alternatively, the CLI can export the data to output files in the specified format, allowing for offline analysis and record-keeping.

## Getting Started

To run the script, you'll need to have Python installed on your machine. Install the required Python libraries listed in the `requirements.txt` file using pip:

```
pip install -r requirements.txt
```

## Dependencies

The script requires the following Python libraries:

- os
- re
- readline
- socket
- getpass
- rich
- importlib
- requests
- yaml
- json
- datetime
- jinja2

These libraries can be installed via pip using the `requirements.txt` file.

## How to Use

The script can be run from a command line terminal using the following command:

```
python telescope.py
```

Once the script is running, you will be prompted to enter your commands at the `telescope#` prompt. The script accepts the following commands:

- `debug enabled`: Enables debug mode.
- `debug disabled`: Disables debug mode.
- `ls`: Lists available resources.
- `show`: Retrieves and displays commands from the execute directory in the specified format (YAML, CSV, JSON, or human-readable).
- `exit`: Exits the program.

## Error Handling

If an error occurs while the script is running, it will be printed to the console with a message indicating that an error occurred.

## Author

Miguel Hernandez
